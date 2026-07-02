# Day 5 3교시 데이터 검증 리포트

## 1. 작성자

- author: kim-juil

## 2. 오늘 주제

S3에서 내려받은 clean 데이터 검증 + 전처리 로직 재사용

## 3. 입력 데이터

| 항목 | 값 |
|---|---|
| local clean file | data/clean/customers_clean_20260606_v2.csv |
| absolute path | /home/soldesk/week2-reproducibility/data/clean/customers_clean_20260606_v2.csv |
| target column | churn |
| execution environment | local_pc_wsl2 |
| OpenShift Local 사용 | 사용하지 않음, 동일 구조 실행 가능성으로 연결 |
| g4dn.xlarge 사용 | 사용하지 않음 |

## 4. 데이터 크기

| 항목 | 값 |
|---|---:|
| row_count | 9 |
| column_count | 29 |

## 5. 컬럼 검증

### expected columns

- customer_id
- age
- gender
- contract_type
- monthly_fee
- support_calls
- usage_days
- churn

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

## 6. 결측치 확인

- 결측치가 남아 있는 컬럼 없음

## 7. dtype 요약

| 구분 | 컬럼 |
|---|---|
| numeric columns | age, monthly_fee, usage_days, support_calls, signup_year, signup_month, last_login_dayofweek, days_since_signup, days_since_last_login, age_was_missing, monthly_fee_was_missing, gender_was_missing, contract_type_was_missing, monthly_fee_outlier, support_calls_outlier, is_high_fee, is_short_user, has_many_support_calls, is_long_contract, churn |
| object columns | customer_id, gender_standard, contract_type_standard, signup_date, last_login_date, last_login_day_name, usage_group, gender, contract_type |
| date candidate columns | signup_date, last_login_date |
| id candidate columns | customer_id |

## 8. target 확인

| 항목 | 값 |
|---|---|
| target column | churn |
| target exists | True |
| target missing count | 0 |
| target unique count | 2 |

### target 분포

- 0: 5
- 1: 4

## 9. leakage 후보 점검

- 명확한 leakage 후보 컬럼 없음

## 10. baseline 준비 판단

| 항목 | 값 |
|---|---|
| baseline_ready | True |
| schema fix 필요 | False |
| 결측치 검토 필요 | False |
| leakage 검토 필요 | False |

## 11. 사용한 재사용 함수

| 함수 | 역할 |
|---|---|
| read_clean_data() | clean CSV 읽기 |
| compare_columns() | expected/actual 컬럼 비교 |
| summarize_missing_values() | 결측치 개수와 비율 요약 |
| summarize_dtypes() | dtype과 컬럼 유형 후보 요약 |
| summarize_target() | target 존재와 분포 확인 |
| detect_possible_leakage_columns() | leakage 후보 컬럼 탐지 |
| validate_customer_schema() | 전체 검증 실행 |

## 12. OpenShift Local 연결

이번 교시에서는 OpenShift Local에 앱을 배포하지 않았다.

하지만 `src/preprocess.py`로 검증 로직을 분리했기 때문에,  
같은 프로젝트 구조와 같은 `.env` 설정을 사용하면  
OpenShift Local 또는 Developer Sandbox에서도 동일한 검증 함수를 재사용할 수 있다.

## 13. g4dn.xlarge 연결

이번 교시에서는 g4dn.xlarge를 사용하지 않았다.

데이터 검증은 pandas 기반 CPU 작업이며 GPU가 필요하지 않다.

이후 GPU 실습에서도 모델 학습 전에 같은 검증 원칙을 사용해야 한다.

## 14. 다음 교시 연결

4교시에서는 검증된 clean 데이터를 기반으로 feature 데이터를 생성한다.

중요한 점은 target인 `churn`을 feature로 넣지 않는 것이다.
