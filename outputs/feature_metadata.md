# Day 5 4교시 Feature 데이터 생성 기록
## 1. 작성자
- author: kim-juil
## 2. 오늘 주제
feature 데이터 생성 + 저장 구조 정리
## 3. 입력 데이터
| 항목 | 값 |
|---|---|
| clean file | data/clean/customers_clean_20260606_v2.csv |
| clean shape | [9, 29] |
| 실행 환경 | 개인 로컬 PC WSL2 |
| OpenShift Local 사용 | 앱 배포 없음, 동일 구조 실행 가능성으로 연결 |
| g4dn.xlarge 사용 | 사용하지 않음 |
## 4. clean 데이터와 feature 데이터 차이
clean 데이터는 분석 가능한 정제 데이터이다.
feature 데이터는 모델 학습에 사용할 입력 데이터이다.
이번 교시에서는 clean 데이터를 기반으로 feature 데이터를 생성했다.
## 5. 생성한 파생 feature
- fee_per_usage_day
- long_usage_flag
- support_call_flag
## 6. feature 정의
| feature | 정의 | 의미 |
|---|---|---|
| fee_per_usage_day | monthly_fee / usage_days | 사용일수 대비 월 요금 |
| support_call_flag | support_calls > 0 | 고객지원 문의 여부 |
| long_usage_flag | usage_days >= 180 | 장기 사용 고객 여부 |
## 7. target 컬럼
- target_col: churn
target인 `churn`은 예측해야 할 정답이므로 feature_cols에 포함하지 않는다.
## 8. 제외 컬럼
- churn
- customer_id
## 9. leakage 후보 컬럼
- 명확한 leakage 후보 없음
## 10. feature 후보 컬럼
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
- gender
- contract_type
- fee_per_usage_day
- support_call_flag
- long_usage_flag
## 11. 범주형 컬럼
- gender
- gender_standard
- contract_type
- contract_type_standard
- usage_group
## 12. 수치형 컬럼
- age
- monthly_fee
- usage_days
- support_calls
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
- is_long_contract
- fee_per_usage_day
- support_call_flag
- long_usage_flag
## 13. 저장 결과
| 파일 | 경로 |
|---|---|
| CSV | data/feature/customers_feature_20260607_v1.csv |
| Parquet | data/feature/customers_feature_20260607_v1.parquet |
## 14. S3 업로드 예정 위치
| 항목 | 값 |
|---|---|
| S3 feature Prefix | users/kim-juil/feature/customers/ |
| 예정 CSV URI | s3://edu-ai-lake/users/kim-juil/feature/customers/customers_feature_20260607_v1.csv |
| 예정 Parquet URI | s3://edu-ai-lake/users/kim-juil/feature/customers/customers_feature_20260607_v1.parquet |
## 15. 값 검증 결과
| 항목 | 값 |
|---|---|
| fee_per_usage_day 결측치 수 | 0 |
| fee_per_usage_day 무한대 수 | 0 |
| support_call_flag unique | [0, 1] |
| long_usage_flag unique | [0, 1] |
## 16. OpenShift Local 연결
이번 교시에서는 OpenShift Local에 앱을 배포하지 않았다.
하지만 feature 생성 로직을 `src/preprocess.py`에 분리했으므로,
같은 프로젝트 구조와 같은 `.env` 설정을 사용하면
OpenShift Local 또는 Developer Sandbox에서도 동일한 feature 생성 함수를 실행할 수 있다.
## 17. g4dn.xlarge 연결
이번 교시에서는 g4dn.xlarge를 사용하지 않았다.
feature 생성은 pandas 기반 CPU 작업이며 GPU가 필요하지 않다.
이후 GPU 실습에서는 이 feature 데이터 또는 split 데이터를 입력으로 사용할 수 있다.
## 18. 다음 교시 연결
5교시에서는 이번 교시에서 만든 feature 데이터를 기반으로
train / validation / test split을 수행한다.
중요한 점은 target 비율을 유지하고,
test 데이터를 마지막까지 아껴 두는 것이다.
