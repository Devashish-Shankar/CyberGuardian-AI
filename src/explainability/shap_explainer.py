"""
CyberGuardian AI

SHAP Explainer

Responsibility:
---------------
Generate SHAP values for a given sample using
a trained tree-based machine learning model.

Supported Models:
-----------------
- Random Forest
- XGBoost (future)
- LightGBM (future)
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import shap


class SHAPExplainer:

    """
    Computes SHAP values for tree-based models.
    """

    def __init__(self, model):

        self.model = model

        self.explainer = shap.TreeExplainer(model)

    def explain(
        self,
        sample: pd.DataFrame
    ) -> np.ndarray:

        if sample is None:
            raise ValueError("Input sample cannot be None.")

        if len(sample) != 1:
            raise ValueError("Exactly one sample expected.")

        shap_values = self.explainer.shap_values(sample)

        shap_values = np.asarray(shap_values)

        # -----------------------------------------
        # Handle different SHAP output formats
        # -----------------------------------------

        if shap_values.ndim == 3:

            # (1, n_features, n_classes)

            shap_values = shap_values[0, :, 1]

        elif shap_values.ndim == 2:

            # (1, n_features)

            shap_values = shap_values[0]

        elif shap_values.ndim == 1:

            pass

        else:

            raise ValueError(
                f"Unsupported SHAP output shape: {shap_values.shape}"
        )

        return shap_values