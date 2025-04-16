import pandas as pd
from sklearn.preprocessing import StandardScaler

def drop_columns(df, columns):
    return df.drop(columns, axis=1)

def scale_features(df):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    return pd.DataFrame(scaled_data, columns=df.columns)