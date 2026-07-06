import pandas as pd


def create_input_dataframe(input_data):
    return pd.DataFrame([input_data])


def encode_and_align(input_df, feature_names):
    encoded_df = pd.get_dummies(input_df)
    aligned_df = encoded_df.reindex(columns=feature_names, fill_value=0)
    return aligned_df