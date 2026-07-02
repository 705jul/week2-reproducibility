# src/io_utils.py

from pathlib import Path
import json

import pandas as pd


def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """
    CSV 파일을 읽어 DataFrame으로 반환한다.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"CSV 파일이 없습니다: {path}")

    return pd.read_csv(path, **kwargs)


def save_csv(
    df: pd.DataFrame,
    path: str | Path,
    index: bool = False,
    encoding: str = "utf-8"
) -> Path:
    """
    DataFrame을 CSV 파일로 저장하고 저장 경로를 반환한다.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=index, encoding=encoding)

    return path


def read_json(path: str | Path) -> dict:
    """
    JSON 파일을 읽어 dict로 반환한다.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"JSON 파일이 없습니다: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict, path: str | Path) -> Path:
    """
    dict 데이터를 JSON 파일로 저장하고 저장 경로를 반환한다.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path
