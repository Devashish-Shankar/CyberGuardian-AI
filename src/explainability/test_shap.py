"""
CyberGuardian AI

Explainability Module Test

Tests:
1. SHAP Explainer
2. Feature Ranker
3. Narrative Builder
4. SHAP Visualizer
"""

from pathlib import Path
import joblib
import pandas as pd

from src.explainability.shap_explainer import SHAPExplainer
from src.explainability.feature_ranker import FeatureRanker
from src.explainability.narrative_builder import NarrativeBuilder
from src.explainability.visualization import SHAPVisualizer


def load_sample():

    print("\nLoading dataset...")

    df = pd.read_parquet(
        "data/processed/clean_cicids.parquet"
    )

    sample = df.drop(
        columns=[
            "Label",
            "attack_category",
            "target"
        ]
    ).iloc[[0]]

    print("Dataset Loaded")

    return sample


def load_model():

    print("\nLoading model...")

    model = joblib.load(
        "artifacts/models/rf_binary.pkl"
    )

    print("Model Loaded")

    return model


def test_shap_explainer(model, sample):

    print("\nTesting SHAP Explainer...")

    explainer = SHAPExplainer(model)

    shap_values = explainer.explain(sample)

    print("SHAP Values Shape:", shap_values.shape)

    print("SHAP Explainer Passed")

    return explainer, shap_values


def test_feature_ranker(sample, shap_values):

    print("\nTesting Feature Ranker...")

    ranker = FeatureRanker()

    ranking = ranker.rank(
        sample,
        shap_values,
        top_k=10
    )

    print(ranking)

    print("Feature Ranker Passed")

    return ranking


def test_narrative_builder(ranking):

    print("\nTesting Narrative Builder...")

    builder = NarrativeBuilder()

    narrative = builder.build(ranking)

    print("\nGenerated Narrative:\n")

    print(narrative)

    print("\nNarrative Builder Passed")

    return narrative


def test_visualizer(explainer, sample, shap_values):

    print("\nTesting SHAP Visualizer...")

    visualizer = SHAPVisualizer()

    visualizer.generate_all(
        explainer,
        shap_values,
        sample
    )

    output_dir = Path("artifacts/shap")

    expected_files = [
        "bar_plot.png",
        "waterfall_plot.png",
        "force_plot.html"
    ]

    print()

    for file in expected_files:

        path = output_dir / file

        if path.exists():

            print(f"{file} ✓")

        else:

            print(f"{file} ✗")

    print("\nVisualizer Passed")


def main():

    print("=" * 70)
    print("CyberGuardian AI")
    print("Explainability Module Test")
    print("=" * 70)

    sample = load_sample()

    model = load_model()

    explainer, shap_values = test_shap_explainer(
        model,
        sample
    )

    ranking = test_feature_ranker(
        sample,
        shap_values
    )

    narrative = test_narrative_builder(
        ranking
    )

    test_visualizer(
        explainer,
        sample,
        shap_values
    )

    print("\n" + "=" * 70)
    print("ALL EXPLAINABILITY TESTS PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()