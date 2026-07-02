# src/s3_utils.py

from pathlib import Path
from datetime import datetime
from typing import Any

import boto3
from botocore.exceptions import BotoCoreError, ClientError


def now_iso() -> str:
    """
    현재 시간을 ISO 형식 문자열로 반환한다.
    """
    return datetime.now().astimezone().isoformat(timespec="seconds")


def build_s3_uri(bucket: str, key: str) -> str:
    """
    bucket과 key로 S3 URI를 만든다.

    예:
    bucket = "edu-ai-lake"
    key = "users/student/clean/customers/file.csv"

    결과:
    s3://edu-ai-lake/users/student/clean/customers/file.csv
    """
    bucket = bucket.replace("s3://", "").strip("/")
    key = key.lstrip("/")

    return f"s3://{bucket}/{key}"


def head_s3_object(bucket: str, key: str) -> dict[str, Any]:
    """
    S3 객체의 metadata를 조회한다.

    Parameters
    ----------
    bucket : str
        S3 bucket name

    key : str
        S3 object key

    Returns
    -------
    dict
        S3 object metadata
    """
    bucket = bucket.replace("s3://", "").strip("/")
    key = key.lstrip("/")

    s3_client = boto3.client("s3")

    try:
        response = s3_client.head_object(
            Bucket=bucket,
            Key=key
        )

        return {
            "success": True,
            "bucket": bucket,
            "key": key,
            "s3_uri": build_s3_uri(bucket, key),
            "content_length": response.get("ContentLength"),
            "content_type": response.get("ContentType"),
            "last_modified": (
                response.get("LastModified").isoformat()
                if response.get("LastModified")
                else None
            ),
            "etag": response.get("ETag"),
            "method": "boto3.head_object",
            "checked_at": now_iso(),
        }

    except (ClientError, BotoCoreError) as e:
        return {
            "success": False,
            "bucket": bucket,
            "key": key,
            "s3_uri": build_s3_uri(bucket, key),
            "error_type": type(e).__name__,
            "error_message": str(e),
            "method": "boto3.head_object",
            "checked_at": now_iso(),
        }


def download_s3_object(
    bucket: str,
    key: str,
    local_path: str | Path
) -> dict[str, Any]:
    """
    S3 객체를 로컬 파일로 다운로드하고 실행 기록을 dict로 반환한다.

    Parameters
    ----------
    bucket : str
        S3 bucket name

    key : str
        S3 object key

    local_path : str | Path
        Local destination path

    Returns
    -------
    dict
        Download result metadata
    """
    bucket = bucket.replace("s3://", "").strip("/")
    key = key.lstrip("/")

    local_path = Path(local_path)
    local_path.parent.mkdir(parents=True, exist_ok=True)

    s3_client = boto3.client("s3")

    started_at = now_iso()

    try:
        s3_client.download_file(
            bucket,
            key,
            str(local_path)
        )

        finished_at = now_iso()

        return {
            "success": True,
            "bucket": bucket,
            "key": key,
            "s3_uri": build_s3_uri(bucket, key),
            "local_path": str(local_path),
            "local_exists": local_path.exists(),
            "local_size_bytes": (
                local_path.stat().st_size
                if local_path.exists()
                else None
            ),
            "started_at": started_at,
            "finished_at": finished_at,
            "method": "boto3.download_file",
        }

    except (ClientError, BotoCoreError) as e:
        finished_at = now_iso()

        return {
            "success": False,
            "bucket": bucket,
            "key": key,
            "s3_uri": build_s3_uri(bucket, key),
            "local_path": str(local_path),
            "local_exists": local_path.exists(),
            "local_size_bytes": (
                local_path.stat().st_size
                if local_path.exists()
                else None
            ),
            "started_at": started_at,
            "finished_at": finished_at,
            "method": "boto3.download_file",
            "error_type": type(e).__name__,
            "error_message": str(e),
        }
