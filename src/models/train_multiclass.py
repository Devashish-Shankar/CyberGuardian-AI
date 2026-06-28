# =====================================================
# CyberGuardian AI
# Multi-Class Attack Classification
# =====================================================

import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    f1_score
)

# =====================================================
# CONFIG
# =====================================================

DATA_PATH = "data/processed/clean_cicids.parquet"

MODEL_DIR = "artifacts/models"

os.makedirs(MODEL_DIR, exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_parquet(DATA_PATH)

print(f"Dataset Shape: {df.shape}")

# =====================================================
# REMOVE VERY RARE CLASSES
# =====================================================

print("\nRemoving Rare Classes (<100 samples)...")

class_counts = df["Label"].value_counts()

valid_classes = class_counts[
    class_counts >= 100
].index

df = df[
    df["Label"].isin(valid_classes)
].copy()

print("\nRemaining Classes:\n")
print(df["Label"].value_counts())

print("\nNumber of Classes:", df["Label"].nunique())

# =====================================================
# ENCODE LABELS
# =====================================================

print("\nEncoding Labels...")

le = LabelEncoder()

df["attack_encoded"] = le.fit_transform(
    df["Label"]
)

label_mapping = dict(
    zip(
        le.classes_,
        le.transform(le.classes_)
    )
)

print("\nLabel Mapping:\n")

for k, v in label_mapping.items():
    print(f"{v} --> {k}")

# =====================================================
# FEATURES AND TARGET
# =====================================================

drop_cols = [
    "Label",
    "attack_category",
    "target",
    "attack_encoded"
]

X = df.drop(columns=drop_cols)

y = df["attack_encoded"]

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

print("\nSplitting Data...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

# =====================================================
# RANDOM FOREST MODEL
# =====================================================

print("\nTraining Random Forest...")

rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    n_jobs=-1,
    random_state=42,
    class_weight="balanced"
)

rf.fit(
    X_train,
    y_train
)

print("Training Completed")

# =====================================================
# PREDICTIONS
# =====================================================

print("\nGenerating Predictions...")

y_pred = rf.predict(X_test)

# =====================================================
# EVALUATION
# =====================================================

print("\n" + "=" * 60)
print("MULTI-CLASS CLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=le.classes_
    )
)

# =====================================================
# ACCURACY
# =====================================================

acc = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(acc)

# =====================================================
# MACRO F1
# =====================================================

macro_f1 = f1_score(
    y_test,
    y_pred,
    average="macro"
)

print("\nMacro F1 Score:")
print(macro_f1)

# =====================================================
# CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix Shape:")
print(cm.shape)

print("\nConfusion Matrix:")
print(cm)

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

importance_df = pd.DataFrame({
    "feature": X.columns,
    "importance": rf.feature_importances_
})

importance_df = importance_df.sort_values(
    by="importance",
    ascending=False
)

print("\n" + "=" * 60)
print("TOP 20 IMPORTANT FEATURES")
print("=" * 60)

print(
    importance_df.head(20)
)

# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(
    rf,
    os.path.join(
        MODEL_DIR,
        "rf_multiclass.pkl"
    )
)

joblib.dump(
    le,
    os.path.join(
        MODEL_DIR,
        "label_encoder.pkl"
    )
)

print("\nModel Saved:")
print("artifacts/models/rf_multiclass.pkl")

print("\nLabel Encoder Saved:")
print("artifacts/models/label_encoder.pkl")

# =====================================================
# SAVE FEATURE IMPORTANCE
# =====================================================

importance_df.to_csv(
    os.path.join(
        MODEL_DIR,
        "feature_importance.csv"
    ),
    index=False
)

print("\nFeature Importance Saved")

print("\n" + "=" * 60)
print("MULTI-CLASS TRAINING COMPLETED")
print("=" * 60)