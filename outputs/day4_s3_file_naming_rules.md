# Day 4 S3 파일명 규칙

## 1. 작성자

- author: kim-juil

## 2. 버킷

- bucket: edu-ai-lake

## 3. 기본 파일명 규칙

```text
{dataset}_{stage}_{yyyymmdd}_v{version}.{ext}
```

## 4. 구성 요소

| 요소 | 의미 | 예시 |
|---|---|---|
| dataset | 데이터셋 이름 | customers |
| stage | 데이터 상태 또는 산출물 유형 | raw, clean, feature, log, report |
| yyyymmdd | 생성일 또는 기준일 | 20260606 |
| version | 버전 | v1, v2 |
| ext | 확장자 | csv, parquet, json, md, ipynb |

## 5. 나쁜 파일명 예시

- customers.csv
- customers_new.csv
- customers_final.csv
- customers_final2.csv
- customers_real_final.csv
- new.csv
- final.csv
- result.csv
- data.csv

## 6. 좋은 파일명 예시

- customers_raw_20260605_v1.csv
- customers_clean_20260606_v2.csv
- customers_feature_20260607_v1.parquet
- run_info_week2_day4_20260606_v1.json
- day4_s3_upload_record_20260606_v1.md

## 7. 데이터 상태별 예시

| stage | 예시 파일명 | 저장 Prefix |
|---|---|---|
| raw | customers_raw_20260605_v1.csv | users/kim-juil/raw/customers/ |
| clean | customers_clean_20260606_v2.csv | users/kim-juil/clean/customers/ |
| feature | customers_feature_20260607_v1.parquet | users/kim-juil/feature/customers/ |
| log | run_info_week2_day4_20260606_v1.json | users/kim-juil/log/week2/ |
| report | day4_s3_data_loading_rules_20260606_v1.md | users/kim-juil/artifact/week2/ |
| notebook | 03_reproducibility_environment_20260606_v1.ipynb | users/kim-juil/notebook/week2/ |

## 8. 버전 증가 기준

- 전처리 기준이 바뀌면 버전을 증가시킨다.
- 컬럼이 추가되면 버전을 증가시킨다.
- 컬럼이 삭제되면 버전을 증가시킨다.
- target 정의가 바뀌면 버전을 증가시킨다.
- feature 생성 기준이 바뀌면 버전을 증가시킨다.
- 단순 파일 이동은 버전 증가 대상이 아닐 수 있으나 기록은 남긴다.

## 9. 파일명 버전과 S3 Versioning의 차이

| 구분 | 파일명 버전 | S3 Versioning |
|---|---|---|
| 예시 | customers_clean_20260606_v2.csv | S3 VersionId |
| 목적 | 사람이 이해하는 데이터 버전 | 덮어쓰기와 삭제 실수 복구 |
| 관리 위치 | 파일명 | S3 내부 객체 버전 |
| 운영 기준 | 반드시 필요 | 버킷 설정으로 보완 |

## 10. 핵심 원칙

좋은 파일명은 파일을 열어보지 않아도  
데이터셋, 상태, 생성일, 버전을 알 수 있어야 한다.
