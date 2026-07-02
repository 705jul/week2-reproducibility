# scripts/check_clean_data.py

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))


from src.paths import get_project_dirs
from src.io_utils import read_csv


def main():
    dirs = get_project_dirs(BASE_DIR)

    clean_file = dirs["clean"] / "customers_clean_20260606_v2.csv"

    df = read_csv(clean_file)

    print("clean_file:", clean_file)
    print("clean data shape:", df.shape)
    print("columns:", list(df.columns))


if __name__ == "__main__":
    main()
