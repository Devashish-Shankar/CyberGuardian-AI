"""
CyberGuardian AI

SHAP Visualization Module

Responsibility
--------------
Generate SHAP visualizations.

Outputs
-------
artifacts/shap/

    bar_plot.png
    waterfall_plot.png
    force_plot.html
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import shap
import numpy as np


class SHAPVisualizer:

    def __init__(self, output_dir: str = "artifacts/shap"):

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    # -------------------------------------------------------------

    def _expected_value(self, explainer):

        """
        Returns expected value for binary classifier.
        Compatible with SHAP >= 0.52
        """

        expected = explainer.explainer.expected_value

        if isinstance(expected, np.ndarray):

            if expected.ndim == 0:
                return float(expected)

            return expected[-1]

        if isinstance(expected, list):

            return expected[-1]

        return expected

    # -------------------------------------------------------------

    def _create_explanation(
        self,
        explainer,
        shap_values,
        sample
    ):

        base_value = self._expected_value(explainer)

        return shap.Explanation(

            values=shap_values,

            base_values=base_value,

            data=sample.iloc[0].values,

            feature_names=sample.columns.tolist()

        )

    # -------------------------------------------------------------

    def save_bar_plot(
        self,
        explainer,
        shap_values,
        sample
    ):

        explanation = self._create_explanation(
            explainer,
            shap_values,
            sample
        )

        plt.figure(figsize=(10, 6))

        shap.plots.bar(
            explanation,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir / "bar_plot.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    # -------------------------------------------------------------

    def save_waterfall_plot(
        self,
        explainer,
        shap_values,
        sample
    ):

        explanation = self._create_explanation(
            explainer,
            shap_values,
            sample
        )

        plt.figure(figsize=(10, 8))

        shap.plots.waterfall(
            explanation,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            self.output_dir / "waterfall_plot.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    # -------------------------------------------------------------

    def save_force_plot(
        self,
        explainer,
        shap_values,
        sample
    ):

        base_value = self._expected_value(explainer)

        force = shap.force_plot(

            base_value,

            shap_values,

            sample.iloc[0].values,

            feature_names=sample.columns.tolist(),

            matplotlib=False

        )

        shap.save_html(

            str(
                self.output_dir / "force_plot.html"
            ),

            force

        )

    # -------------------------------------------------------------

    def generate_all(
        self,
        explainer,
        shap_values,
        sample
    ):

        print("\nGenerating SHAP visualizations...")

        self.save_bar_plot(
            explainer,
            shap_values,
            sample
        )

        print("✓ Bar Plot")

        self.save_waterfall_plot(
            explainer,
            shap_values,
            sample
        )

        print("✓ Waterfall Plot")

        self.save_force_plot(
            explainer,
            shap_values,
            sample
        )

        print("✓ Force Plot")

        print("\nAll SHAP visualizations generated successfully.")