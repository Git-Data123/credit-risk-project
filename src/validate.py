import pandas as pd

def validate_data(df):
    print("\n--- VALIDATION REPORT ---\n")

    print("Missing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

if __name__ == "__main__":
    df = pd.read_csv("SampleSuperstore.csv")
    validate_data(df)