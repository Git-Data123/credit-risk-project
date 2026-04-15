from src.ingest import load_data
from src.validate import validate_data

df = load_data()
validate_data(df)