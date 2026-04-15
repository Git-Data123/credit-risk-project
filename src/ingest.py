import pandas as pd

def load_data():
    df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding="latin1")
    print("Data loaded successfully")
    print(df.shape)
    return df

if __name__ == "__main__":
    load_data()
