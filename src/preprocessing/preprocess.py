from pathlib import Path
import pandas as pd

RAW_DIR = "data/raw"

def load_data():

    files = list(Path(RAW_DIR).glob("*.parquet"))

    dfs = []

    for file in files:

        df = pd.read_parquet(file)

        attack_name = file.stem.split("-")[0]

        df["attack_category"] = attack_name

        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)

def audit_data(df):

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum().sort_values(ascending=False).head(20))

    print("\nDuplicates:")
    print(df.duplicated().sum())

    print("\nLabel Distribution:")
    print(df["Label"].value_counts())
    
import numpy as np

def clean_data(df):

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:

        df[col] = df[col].fillna(df[col].median())

    return df


def create_binary_target(df):

    df["target"] = df["Label"].apply(
        lambda x: 0 if str(x).lower() == "benign" else 1
    )

    return df


from sklearn.preprocessing import LabelEncoder

def encode_attack_type(df):

    le = LabelEncoder()

    df["attack_encoded"] = le.fit_transform(df["Label"])

    return df, le


def save_clean_data(df):

    df.to_parquet(
        "data/processed/clean_cicids.parquet",
        index=False
    )

    print("Dataset Saved")
    
if __name__ == "__main__":

    df = load_data()

    audit_data(df)

    df = clean_data(df)

    df = create_binary_target(df)

    save_clean_data(df)

    print(df.head())