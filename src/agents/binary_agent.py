import joblib
import pandas as pd


class BinaryDetectionAgent:

    def __init__(self):

        self.model = joblib.load(
            "artifacts/models/rf_binary.pkl"
        )

    def detect(
        self,
        sample: pd.DataFrame
    ):

        prediction = self.model.predict(sample)[0]

        probability = self.model.predict_proba(
            sample
        )[0]

        confidence = probability.max()

        return {

            "prediction": int(prediction),

            "confidence": float(confidence)

        }