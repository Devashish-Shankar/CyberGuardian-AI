"""
CyberGuardian AI

Feature Ranker

Responsibility:
---------------
Convert SHAP values into a ranked feature importance table.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class FeatureRanker:
    """
    Ranks features based on absolute SHAP importance.
    """

    def rank(
        self,
        sample: pd.DataFrame,
        shap_values: np.ndarray,
        top_k: int = 10
    ) -> pd.DataFrame:

        # -----------------------------
        # Validation
        # -----------------------------

        if sample is None:
            raise ValueError("Sample cannot be None.")

        if shap_values is None:
            raise ValueError("SHAP values cannot be None.")

        if len(sample) != 1:
            raise ValueError(
                "FeatureRanker expects exactly one sample."
            )

        if len(shap_values) != sample.shape[1]:
            raise ValueError(
                "Mismatch between number of features and SHAP values."
            )

        # -----------------------------
        # Build dataframe
        # -----------------------------

        ranking = pd.DataFrame({

            "feature": sample.columns,

            "feature_value": sample.iloc[0].values,

            "shap_value": shap_values,

            "importance": np.abs(shap_values)

        })

        # -----------------------------
        # Sort
        # -----------------------------

        ranking = ranking.sort_values(
            by="importance",
            ascending=False
        ).reset_index(drop=True)

        return ranking.head(top_k)