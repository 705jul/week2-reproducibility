# src/preprocess.py

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def read_clean_data(path: str | Path) -> pd.DataFrame:
    """
    clean CSV 파일을 읽고 DataFrame을 반환한다.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"clean data file not found: {path}")

    return pd.read_csv(path)


def compare_columns(
    df: pd.DataFrame,
    expected_columns: list[str],
) -> dict[str, Any]:
    """
    기대 컬럼과 실제 컬럼을 비교한다.
    """
    actual_columns = list(df.columns)

    expected_set = set(expected_columns)
    actual_set = set(actual_columns)

    missing_columns = sorted(list(expected_set - actual_set))
    extra_columns = sorted(list(actual_set - expected_set))

    return {
        "expected_columns": expected_columns,
        "actual_columns": actual_columns,
        "missing_columns": missing_columns,
        "extra_columns": extra_columns,
        "has_required_columns": len(missing_columns) == 0,
    }


def summarize_missing_values(df: pd.DataFrame) -> dict[str, Any]:
    """
    컬럼별 결측치 개수와 비율을 요약한다.
    """
    missing_count = df.isna().sum()
    missing_ratio = df.isna().mean() * 100

    missing_columns = []

    for col in df.columns:
        count = int(missing_count[col])
        ratio = float(round(missing_ratio[col], 2))

        if count > 0:
            missing_columns.append(
                {
                    "column": col,
                    "missing_count": count,
                    "missing_ratio_percent": ratio,
                }
            )

    return {
        "total_missing_count": int(missing_count.sum()),
        "columns_with_missing": missing_columns,
        "has_missing_values": int(missing_count.sum()) > 0,
    }


def summarize_dtypes(df: pd.DataFrame) -> dict[str, Any]:
    """
    pandas dtype과 기본 컬럼 유형 후보를 요약한다.
    """
    dtype_map = {
        col: str(dtype)
        for col, dtype in df.dtypes.items()
    }

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    object_columns = df.select_dtypes(include=["object"]).columns.tolist()
    bool_columns = df.select_dtypes(include=["bool"]).columns.tolist()

    date_candidate_columns = [
        col for col in df.columns
        if (
            "date" in col.lower()
            or "dt" in col.lower()
            or "time" in col.lower()
        )
    ]

    id_candidate_columns = [
        col for col in df.columns
        if (
            col.lower().endswith("_id")
            or col.lower() in ["id", "customer_id", "user_id"]
        )
    ]

    return {
        "dtype_map": dtype_map,
        "numeric_columns": numeric_columns,
        "object_columns": object_columns,
        "bool_columns": bool_columns,
        "date_candidate_columns": date_candidate_columns,
        "id_candidate_columns": id_candidate_columns,
    }


def summarize_target(
    df: pd.DataFrame,
    target_column: str,
) -> dict[str, Any]:
    """
    target 컬럼 존재 여부, 결측치, 값 분포를 요약한다.
    """
    exists = target_column in df.columns

    if not exists:
        return {
            "target_column": target_column,
            "target_exists": False,
            "target_missing_count": None,
            "target_missing_ratio_percent": None,
            "target_unique_count": None,
            "target_distribution_count": {},
            "target_distribution_ratio": {},
        }

    target_series = df[target_column]

    count = target_series.value_counts(dropna=False)
    ratio = target_series.value_counts(normalize=True, dropna=False)

    return {
        "target_column": target_column,
        "target_exists": True,
        "target_missing_count": int(target_series.isna().sum()),
        "target_missing_ratio_percent": float(
            round(target_series.isna().mean() * 100, 2)
        ),
        "target_unique_count": int(target_series.nunique(dropna=True)),
        "target_distribution_count": {
            str(k): int(v)
            for k, v in count.items()
        },
        "target_distribution_ratio": {
            str(k): float(round(v, 4))
            for k, v in ratio.items()
        },
    }


def detect_possible_leakage_columns(
    df: pd.DataFrame,
    target_column: str,
    extra_keywords: list[str] | None = None,
) -> dict[str, Any]:
    """
    이름 기준으로 데이터 누수 후보 컬럼을 탐지한다.
    """
    leakage_keywords = [
        "churn",
        "label",
        "target",
        "result",
        "outcome",
        "after",
        "future",
        "next",
        "retention_result",
    ]

    if extra_keywords:
        leakage_keywords.extend(extra_keywords)

    possible_leakage_columns = []
    target_column_lower = target_column.lower()

    for col in df.columns:
        col_lower = col.lower()

        if col_lower == target_column_lower:
            continue

        if any(keyword in col_lower for keyword in leakage_keywords):
            possible_leakage_columns.append(col)

    return {
        "target_column": target_column,
        "leakage_keywords": leakage_keywords,
        "possible_leakage_columns": possible_leakage_columns,
        "possible_leakage_columns_count": len(possible_leakage_columns),
    }


def validate_customer_schema(
    df: pd.DataFrame,
    expected_columns: list[str],
    target_column: str = "churn",
) -> dict[str, Any]:
    """
    고객 이탈 clean 데이터의 기본 검증 결과를 dict로 반환한다.
    """
    column_result = compare_columns(df, expected_columns)
    missing_result = summarize_missing_values(df)
    dtype_result = summarize_dtypes(df)
    target_result = summarize_target(df, target_column)
    leakage_result = detect_possible_leakage_columns(df, target_column)

    row_count = int(len(df))
    column_count = int(len(df.columns))

    baseline_ready = (
        row_count > 0
        and column_count > 0
        and column_result["has_required_columns"]
        and target_result["target_exists"]
        and target_result["target_missing_count"] == 0
        and target_result["target_unique_count"] is not None
        and target_result["target_unique_count"] >= 2
    )

    return {
        "row_count": row_count,
        "column_count": column_count,
        "columns": column_result,
        "missing_values": missing_result,
        "dtypes": dtype_result,
        "target": target_result,
        "leakage": leakage_result,
        "baseline_ready": bool(baseline_ready),
    }


def create_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    4교시 feature 생성에서 사용할 기본 함수 자리.

    3교시에서는 함수 구조만 예고하고,
    본격 feature 생성은 4교시에서 진행한다.
    """
    feature_df = df.copy()

    return feature_df

import numpy as np

def create_basic_customer_features(
    df: pd.DataFrame,
    monthly_fee_col: str = "monthly_fee",
    usage_days_col: str = "usage_days",
    support_calls_col: str = "support_calls",
    long_usage_threshold: int = 180,
) -> pd.DataFrame:
    """
    고객 이탈 예측용 기본 파생 feature를 생성한다.

    생성 feature
    ----------
    fee_per_usage_day:
        usage_days 대비 monthly_fee

    support_call_flag:
        support_calls > 0 여부

    long_usage_flag:
        usage_days >= long_usage_threshold 여부

    주의
    ----------
    원본 df를 직접 수정하지 않고 복사본 feature_df를 반환한다.
    """
    feature_df = df.copy()

    required_cols = [
        monthly_fee_col,
        usage_days_col,
        support_calls_col,
    ]

    missing_cols = [
        col for col in required_cols
        if col not in feature_df.columns
    ]

    if missing_cols:
        raise KeyError(f"feature 생성에 필요한 컬럼이 없습니다: {missing_cols}")

    usage_days = feature_df[usage_days_col].replace(0, np.nan)

    feature_df["fee_per_usage_day"] = (
        feature_df[monthly_fee_col] / usage_days
    )

    feature_df["fee_per_usage_day"] = feature_df["fee_per_usage_day"].replace(
        [np.inf, -np.inf],
        np.nan
    )

    feature_df["fee_per_usage_day"] = feature_df["fee_per_usage_day"].fillna(0)

    feature_df["support_call_flag"] = (
        feature_df[support_calls_col] > 0
    ).astype(int)

    feature_df["long_usage_flag"] = (
        feature_df[usage_days_col] >= long_usage_threshold
    ).astype(int)

    return feature_df


def create_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Day 5 4교시에서 사용하는 기본 feature 생성 함수.

    기존 Notebook에서 create_basic_features(df)를 계속 사용할 수 있도록
    create_basic_customer_features()를 감싼다.
    """
    return create_basic_customer_features(df)
