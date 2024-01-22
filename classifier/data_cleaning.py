import pandas as pd
from pathlib import Path


def clean_training_data(df: pd.DataFrame) -> pd.DataFrame:
    # clean up the column names first
    df.columns = [x.lower().replace(' ', '_') for x in df.columns]
    # remove the dollar sign from the amount as well as the comma separating M, K, etc.
    df["amount"] = df["amount"].apply(lambda x: x.replace(',', '').replace('$', '').replace('−', '-'))
    df["amount"] = df["amount"].astype(float)
    # lower the label
    df["category"] = df["category"].str.lower()
    return df


def main():
    df = pd.read_csv(Path(Path().absolute(), "../training_data.csv"))
    cleaned_df = clean_training_data(df)


if __name__ == "__main__":
    main()