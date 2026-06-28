import pandas as pd

df = pd.read_parquet(
    "data/processed/clean_cicids.parquet"
)

print("\nTarget Distribution:\n")
print(df["target"].value_counts())

print("\nPercentage:\n")
print(
    df["target"].value_counts(normalize=True) * 100
)