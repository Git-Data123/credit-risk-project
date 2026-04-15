import pandas as pd

def load_data():
    df = pd.read_csv("SampleSuperstore.csv")
    print("Data loaded successfully")
    print(df.shape)
    return df

if __name__ == "__main__":
    load_data()