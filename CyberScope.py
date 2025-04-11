from google.colab import drive
import os
import pandas as pd

drive.mount('/content/drive', force_remount=True)
file_path = "/content/drive/MyDrive/pfa/cyber_data.csv"

if not os.path.exists(file_path):
    print(f"ERROR: The file {file_path} does not exist. Please check the path!")
else:
    print("File found, loading...")
    df = pd.read_csv(file_path)
    print("Preview of the first rows:")
    print(df.head())

# General dataset info & summary statistics
print("
 Info about the dataset :")
df.info()
df.describe(include='all')

#clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
print("Cleaned column names:")
print(df.columns.tolist())

