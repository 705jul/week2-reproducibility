# 2주차 Day 5 4교시 실습 기록지

## 작성자

## 1. 오늘 주제

feature 데이터 생성 + 저장 구조 정리

## 2. 입력 데이터

- clean file:
- clean shape:
- S3 source URI:

## 3. clean 데이터와 feature 데이터 차이

- clean 데이터:
- feature 데이터:

## 4. target 컬럼

- target_col:

## 5. 제외 컬럼

- drop_cols:

## 6. 생성한 feature

### fee_per_usage_day

- 정의:
- 의미:
- 결측치 수:
- 무한대 수:

### support_call_flag

- 정의:
- 의미:
- unique 값:

### long_usage_flag

- 정의:
- 의미:
- unique 값:

## 7. feature 후보 컬럼

- feature_cols:

## 8. 범주형 컬럼

- categorical_cols:

## 9. 수치형 컬럼

- numeric_cols:

## 10. 저장 파일

| 구분 | 경로 |
|---|---|
| CSV | data/feature/customers_feature_20260607_v1.csv |
| Parquet | data/feature/customers_feature_20260607_v1.parquet |
| metadata JSON | outputs/feature_metadata.json |
| metadata Markdown | outputs/feature_metadata.md |

## 11. S3 업로드 예정 Prefix

- feature Prefix:

## 12. OpenShift Local 연결

- OpenShift Local에서 같은 feature 생성 코드를 실행하려면 무엇이 같아야 하는가?

## 13. g4dn 연결

- 이번 교시에서 g4dn을 사용하지 않는 이유는?
- 이후 GPU 실습에서 feature 데이터가 왜 필요한가?

## 14. 오늘 배운 핵심

-

## 15. 다음 교시에서 할 일

train / validation / test split + leakage 점검
