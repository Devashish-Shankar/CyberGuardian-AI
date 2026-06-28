import shap
import joblib
import pandas as pd


class SHAPExplainer:

    def __init__(
        self,
        model_path
    ):

        self.model = joblib.load(model_path)

        self.explainer = shap.TreeExplainer(
            self.model
        )

    def explain(
        self,
        sample: pd.DataFrame
    ):

        shap_values = self.explainer.shap_values(
            sample
        )

        return shap_values