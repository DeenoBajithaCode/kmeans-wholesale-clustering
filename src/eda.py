import pandas as pd
from ydata_profiling import ProfileReport

def load_data(filepath):
    return pd.read_csv(filepath)

def generate_profile_report(df, output_path):
    profile = ProfileReport(df, title="Wholesale Customer Profiling Report")
    profile.to_file(output_path)
    return profile