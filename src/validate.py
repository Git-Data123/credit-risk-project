import pandas as pd

def validate_data(df):
    print("\n--- VALIDATION REPORT ---\n")
    print("Missing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

if __name__ == "__main__":
    df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding="latin1")
    validate_data(df)
