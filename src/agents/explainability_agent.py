"""
==========================================================
CyberGuardian AI

Explainability Agent

Responsible for generating explainable AI insights
using the Explainability Module.

Author: Devashish
==========================================================
"""

from __future__ import annotations

import joblib
import pandas as pd

from src.agents.base_agent import BaseAgent

from src.explainability.shap_explainer import SHAPExplainer
from src.explainability.feature_ranker import FeatureRanker
from src.explainability.narrative_builder import NarrativeBuilder
from src.explainability.visualization import SHAPVisualizer


MODEL_PATH = "artifacts/models/rf_multiclass.pkl"


class ExplainabilityAgent(BaseAgent):
    """
    Generates explainability information
    for a prediction.
    """

    def __init__(self) -> None:

        # ---------------------------------------------
        # Load trained model
        # ---------------------------------------------

        self.model = joblib.load(
            MODEL_PATH
        )

        # ---------------------------------------------
        # Explainability Components
        # ---------------------------------------------

        self.explainer = SHAPExplainer(
            self.model
        )

        self.ranker = FeatureRanker()

        self.narrative_builder = NarrativeBuilder()

        self.visualizer = SHAPVisualizer()

    # =====================================================
    # Public API
    # =====================================================

    def run(
        self,
        sample: pd.DataFrame
    ) -> dict:

        if not isinstance(sample, pd.DataFrame):

            raise TypeError(
                "Sample must be a pandas DataFrame."
            )

        if sample.empty:

            raise ValueError(
                "Input DataFrame cannot be empty."
            )

        # ---------------------------------------------
        # Generate SHAP Values
        # ---------------------------------------------

        shap_values = self.explainer.explain(
            sample
        )

        # ---------------------------------------------
        # Rank Features
        # ---------------------------------------------

        ranked_features = self.ranker.rank(

            sample=sample,

            shap_values=shap_values,

            top_k=10

        )

        # ---------------------------------------------
        # Build Human Readable Narrative
        # ---------------------------------------------

        narrative = self.narrative_builder.build(
            ranked_features
        )

        # ---------------------------------------------
        # Generate Visualizations
        # ---------------------------------------------

        self.visualizer.generate_all(

            explainer=self.explainer,

            shap_values=shap_values,

            sample=sample

        )

        # ---------------------------------------------
        # Final Response
        # ---------------------------------------------

        return {

            "top_features": ranked_features,

            "narrative": narrative,

            "shap_values": shap_values.tolist(),

            "visualization_generated": True

        }