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

# expected date format pattern
date_pattern = r'^\d{2}/\d{2}/\d{4} 0:00$'

# nbr of rows match the format
valid_dates_count = df['attackdate'].str.match(date_pattern).sum()
print(f"Number of rows that match the '%d/%m/%Y 0:00' format: {valid_dates_count}")

df['attackdate'] = df['attackdate'].str.replace('0:00', '').str.strip()
df['attackdate'] = pd.to_datetime(df['attackdate'], format="%d/%m/%Y")

