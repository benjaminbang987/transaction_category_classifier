import pandas as pd
import re


def model_building_xgb(df: pd.DataFrame):
    """
    Besides the amount and the date field, the string "description" field contains the most information.
    We can extract features from it and run XGBoost, or we can fine-tune the pretrained Embeddings Model
    Let's do the first one with XGBoost.
    """
    # let's create some features based off of "Description"
    # Rent feature
    df["is_rent"] = df["description"].str.match("rent", case=False)
    # Utility features
    df["is_pge"] = df["description"].str.contains("[\s\S]*pg[\s\S]*e", flags=re.IGNORECASE, regex=True)
    df["is_xfinity"] = df["description"].str.contains("[\s\S]*xfinity[\s\S]*|[\s\S]*comcast[\s\S]*",
                                                      flags=re.IGNORECASE, regex=True)
    # Auto Features
    df["is_gas"] = df["description"].str.contains("[\s]gas", case=False)

