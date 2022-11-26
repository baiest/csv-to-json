import csv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def converter_csv_to_json(path_csv):
    data = []
    with open(BASE_DIR / path_csv, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [rows for rows in reader]
    return data