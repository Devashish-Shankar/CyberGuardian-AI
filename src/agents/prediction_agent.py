"""
==========================================================
CyberGuardian AI

Prediction Agent

Responsible for:
- Binary Attack Detection
- Multi-Class Attack Classification

Author: Devashish
==========================================================
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from src.agents.base_agent import BaseAgent


MODEL_DIR = Path("artifacts/models")


class PredictionAgent(BaseAgent):
    """
    Performs binary and multi-class attack prediction.
    """

    def __init__(self) -> None:

        self.binary_model = self._load_model(
            MODEL_DIR / "rf_binary.pkl"
        )

        self.multiclass_model = self._load_model(
            MODEL_DIR / "rf_multiclass.pkl"
        )

        self.label_encoder = self._load_model(
            MODEL_DIR / "label_encoder.pkl"
        )

    # =====================================================
    # Private Methods
    # =====================================================

    def _load_model(self, path: Path):

        if not path.exists():

            raise FileNotFoundError(
                f"Model not found:\n{path}"
            )

        return joblib.load(path)

    def _validate_input(
        self,
        sample: pd.DataFrame
    ) -> None:

        if not isinstance(sample, pd.DataFrame):

            raise TypeError(
                "Input must be a pandas DataFrame."
            )

        if sample.empty:

            raise ValueError(
                "Input DataFrame is empty."
            )

        if len(sample) != 1:

            raise ValueError(
                "PredictionAgent expects exactly one sample."
            )

    def _binary_predict(
        self,
        sample: pd.DataFrame
    ) -> tuple[int, float]:

        prediction = int(
            self.binary_model.predict(sample)[0]
        )

        confidence = float(

            np.max(

                self.binary_model.predict_proba(sample)

            )

        )

        return prediction, confidence

    def _multiclass_predict(
        self,
        sample: pd.DataFrame
    ) -> dict:

        prediction = int(
            self.multiclass_model.predict(sample)[0]
        )

        probabilities = self.multiclass_model.predict_proba(
            sample
        )[0]

        confidence = float(
            np.max(probabilities)
        )

        attack_name = self.label_encoder.inverse_transform(
            [prediction]
        )[0]

        top_indices = np.argsort(
            probabilities
        )[::-1][:3]

        top_predictions = []

        for idx in top_indices:

            top_predictions.append({

                "attack": self.label_encoder.inverse_transform(
                    [idx]
                )[0],

                "probability": round(
                    float(probabilities[idx]) * 100,
                    2
                )

            })

        return {

            "attack_name": attack_name,

            "confidence": round(
                confidence * 100,
                2
            ),

            "top_predictions": top_predictions

        }

    # =====================================================
    # Public API
    # =====================================================

    def run(
        self,
        sample: pd.DataFrame
    ) -> dict:

        self._validate_input(sample)

        prediction, confidence = self._binary_predict(
            sample
        )

        if prediction == 0:

            return {

                "is_attack": False,

                "attack_name": "Benign",

                "confidence": round(
                    confidence * 100,
                    2
                ),

                "top_predictions": []

            }

        result = self._multiclass_predict(
            sample
        )

        return {

            "is_attack": True,

            "attack_name": result["attack_name"],

            "confidence": result["confidence"],

            "top_predictions": result["top_predictions"]

        }