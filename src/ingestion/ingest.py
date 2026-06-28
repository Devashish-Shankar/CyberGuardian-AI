from pathlib import Path
import pandas as pd

RAW_DIR = "data/raw"


def load_all_data():

    files = list(Path(RAW_DIR).glob("*.parquet"))

    dfs = []

    for file in files:

        print(f"Loading {file.name}")

        df = pd.read_parquet(file)

        attack_name = file.stem.split("-")[0]

        df["attack_category"] = attack_name

        dfs.append(df)

    final_df = pd.concat(dfs, ignore_index=True)

    print("Total Rows:", len(final_df))
    print("Total Columns:", final_df.shape[1])

    return final_df


if __name__ == "__main__":

    data = load_all_data()

    print(data.head())