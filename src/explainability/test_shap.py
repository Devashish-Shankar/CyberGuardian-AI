import pandas as pd

from src.explainability.shap_explainer import SHAPExplainer

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

explainer = SHAPExplainer(
    "artifacts/models/rf_binary.pkl"
)

values = explainer.explain(
    sample
)

print(values)