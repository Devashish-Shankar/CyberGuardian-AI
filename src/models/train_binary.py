import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# ------------------------
# Load Data
# ------------------------

df = pd.read_parquet(
    "data/processed/clean_cicids.parquet"
)

print("Dataset Shape:", df.shape)

# ------------------------
# Features and Target
# ------------------------

drop_cols = [
    "Label",
    "attack_category",
    "target"
]

X = df.drop(columns=drop_cols)

y = df["target"]

print("Feature Shape:", X.shape)

# ------------------------
# Train Test Split
# ------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

# ------------------------
# Random Forest
# ------------------------

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    n_jobs=-1,
    random_state=42,
    class_weight="balanced"
)

print("Training Started...")

model.fit(
    X_train,
    y_train
)

print("Training Completed")

# ------------------------
# Predictions
# ------------------------

preds = model.predict(X_test)

# ------------------------
# Metrics
# ------------------------

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        preds
    )
)

print("\nConfusion Matrix\n")

print(
    confusion_matrix(
        y_test,
        preds
    )
)

print("\nROC AUC\n")

print(
    roc_auc_score(
        y_test,
        preds
    )
)

# ------------------------
# Feature Importance
# ------------------------

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

importance = importance.sort_values(
    by="importance",
    ascending=False
)

print("\nTop 20 Features\n")

print(
    importance.head(20)
)

# ------------------------
# Save Model
# ------------------------

joblib.dump(
    model,
    "artifacts/models/rf_binary.pkl"
)

print("\nModel Saved Successfully")