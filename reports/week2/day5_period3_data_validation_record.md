# 2주차 Day 5 3교시 실습 기록지

## 작성자

- author: kim-juil

## 1. 오늘 주제

데이터 검증 + 전처리 로직 재사용

## 2. 입력 데이터

- local clean file: data/clean/customers_clean_20260606_v2.csv
- S3 bucket: edu-ai-lake
- S3 key: users/kim-juil/clean/customers/customers_clean_20260606_v2.csv
- S3 URI: s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv

## 3. 데이터 크기

- rows: 9
- columns: 29

## 4. 컬럼 검증

### expected columns

- customer_id
- age
- gender
- contract_type
- monthly_fee
- support_calls
- usage_days
- churn

### actual columns

- customer_id
- age
- monthly_fee
- usage_days
- support_calls
- gender_standard
- contract_type_standard
- signup_date
- last_login_date
- signup_year
- signup_month
- last_login_dayofweek
- last_login_day_name
- days_since_signup
- days_since_last_login
- age_was_missing
- monthly_fee_was_missing
- gender_was_missing
- contract_type_was_missing
- monthly_fee_outlier
- support_calls_outlier
- is_high_fee
- is_short_user
- has_many_support_calls
- usage_group
- is_long_contract
- churn
- gender
- contract_type

### missing columns

- 없음

### extra columns

- age_was_missing
- contract_type_standard
- contract_type_was_missing
- days_since_last_login
- days_since_signup
- gender_standard
- gender_was_missing
- has_many_support_calls
- is_high_fee
- is_long_contract
- is_short_user
- last_login_date
- last_login_day_name
- last_login_dayofweek
- monthly_fee_outlier
- monthly_fee_was_missing
- signup_date
- signup_month
- signup_year
- support_calls_outlier
- usage_group

## 5. 결측치 확인

- 결측치가 있는 컬럼:

- 결측치가 있는 컬럼 없음

- 결측치 비율이 높은 컬럼:

- 결측치 비율이 높은 컬럼 없음

- 처리 필요 여부: False

## 6. dtype 확인

- 수치형 컬럼:

- age
- monthly_fee
- usage_days
- support_calls
- signup_year
- signup_month
- last_login_dayofweek
- days_since_signup
- days_since_last_login
- age_was_missing
- monthly_fee_was_missing
- gender_was_missing
- contract_type_was_missing
- monthly_fee_outlier
- support_calls_outlier
- is_high_fee
- is_short_user
- has_many_support_calls
- is_long_contract
- churn

- 범주형 또는 object 컬럼:

- customer_id
- gender_standard
- contract_type_standard
- signup_date
- last_login_date
- last_login_day_name
- usage_group
- gender
- contract_type

- 날짜형 후보 컬럼:

- signup_date
- last_login_date

- 식별자 후보 컬럼:

- customer_id

## 7. target 확인

- target 컬럼: churn
- target 존재 여부: True
- target 결측치 수: 0
- target class 개수: 2
- target 분포:

- 0: 5
- 1: 4

## 8. leakage 점검

- target과 유사한 feature 후보:

- 없음

- 미래 정보 컬럼 후보:

- 없음

- 식별자 컬럼 후보:

- customer_id

- 제거 또는 검토할 컬럼:

- customer_id

## 9. baseline 준비 가능 여부

- 가능 여부: True
- 이유:

- 필수 컬럼, target, 데이터 크기 조건을 1차로 만족했다.

- 추가 확인 필요 사항:

- extra columns 중 leakage 후보가 있는지 확인한다.
- 식별자 컬럼은 feature에서 제외할지 검토한다.
- target 컬럼은 feature에 넣지 않는다.

## 10. 작성한 산출물

| 산출물 | 경로 |
|---|---|
| 데이터 검증 JSON | outputs/data_validation_report.json |
| 데이터 검증 Markdown | outputs/data_validation_report.md |
| 전처리 재사용 모듈 | src/preprocess.py |

## 11. OpenShift Local 연결

- OpenShift Local에서 같은 검증 로직을 실행하려면 무엇이 같아야 하는가?
- 같은 프로젝트 폴더 구조를 사용해야 한다.
- 같은 `requirements.txt`를 사용해야 한다.
- 같은 `.env.example` 구조를 유지해야 한다.
- 같은 `src/preprocess.py` 모듈을 사용할 수 있어야 한다.
- S3 bucket, S3 key, local clean file 경로를 환경 변수 또는 ConfigMap으로 주입할 수 있어야 한다.

## 12. g4dn 연결

- 이번 교시에서 g4dn을 사용하지 않는 이유는?
  - 데이터 검증은 pandas 기반 CPU 작업이므로 GPU가 필요하지 않다.

- GPU 학습 전에 데이터 검증이 필요한 이유는?
  - 잘못된 데이터로 GPU 학습을 실행하면 시간과 비용이 낭비된다.
  - target 누락, leakage, 결측치, 컬럼 불일치를 먼저 확인해야 한다.
  - 검증된 feature 데이터만 GPU 학습 단계로 넘기는 것이 안전하다.

## 13. 오늘 배운 핵심

- 데이터 검증은 모델링 전에 반드시 수행해야 한다.
- expected columns와 actual columns를 비교해야 한다.
- target 컬럼은 존재 여부, 결측치, class 개수를 확인해야 한다.
- leakage 후보 컬럼은 feature로 사용하기 전에 반드시 검토해야 한다.
- 검증 로직은 `src/preprocess.py`로 분리하면 재사용할 수 있다.

## 14. 다음 교시에서 할 일

feature 데이터 생성 + 저장 구조 정리
