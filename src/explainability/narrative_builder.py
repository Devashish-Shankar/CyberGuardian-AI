"""
CyberGuardian AI

Narrative Builder

Responsibility:
---------------
Convert ranked SHAP features into a deterministic,
human-readable explanation.
"""

from __future__ import annotations

import pandas as pd


class NarrativeBuilder:

    """
    Generates deterministic explanations from
    ranked SHAP features.
    """

    def build(
        self,
        ranking: pd.DataFrame,
        top_k: int = 5
    ) -> str:

        if ranking is None:
            raise ValueError("Ranking cannot be None.")

        if ranking.empty:
            raise ValueError("Ranking dataframe is empty.")

        features = ranking["feature"].head(top_k).tolist()

        if len(features) == 1:

            return (
                f"The prediction was primarily influenced by "
                f"{features[0]}."
            )

        if len(features) == 2:

            return (
                f"The prediction was primarily influenced by "
                f"{features[0]} and {features[1]}."
            )

        explanation = ", ".join(features[:-1])

        explanation += f" and {features[-1]}"

        return (
            f"The model's prediction was primarily driven by "
            f"{explanation}. "
            f"These features had the strongest influence on the final prediction."
        )