"""
CyberGuardian AI

Multi-Class Detection Agent
"""

import joblib
import pandas as pd
import numpy as np


class MultiClassDetectionAgent:

    def __init__(self):

        self.model = joblib.load(
            "artifacts/models/rf_multiclass.pkl"
        )

        self.encoder = joblib.load(
            "artifacts/models/label_encoder.pkl"
        )

    def detect(
        self,
        sample: pd.DataFrame
    ) -> dict:

        prediction = self.model.predict(sample)[0]

        probabilities = self.model.predict_proba(sample)[0]

        attack_name = self.encoder.inverse_transform(
            [prediction]
        )[0]

        confidence = float(np.max(probabilities))

        top3_idx = np.argsort(probabilities)[::-1][:3]

        top_predictions = []

        for idx in top3_idx:

            top_predictions.append({

                "attack": self.encoder.inverse_transform([idx])[0],

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


if __name__ == "__main__":

    import pandas as pd

    df = pd.read_parquet(
        "data/processed/clean_cicids.parquet"
    )

    sample = df.drop(
        columns=[
            "Label",
            "attack_category",
            "target"
        ]
    ).iloc[[100]]

    agent = MultiClassDetectionAgent()

    result = agent.detect(sample)

    print(result)