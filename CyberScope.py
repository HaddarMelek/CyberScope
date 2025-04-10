import os
import pandas as pd

file_path = "/Users/macbook/ML/pfa/CyberScope/cyber_data.csv"

if not os.path.exists(file_path):
    print(f"ERROR: The file {file_path} does not exist. Please check the path!")
else:
    print("File found, loading...")
    df = pd.read_csv(file_path)
    print("Preview of the first rows:")
    print(df.head())
