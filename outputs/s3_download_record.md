# Day 5 2교시 S3 다운로드 기록
## 1. 작성자
- author: kim-juil
## 2. 오늘 주제
S3에서 clean 데이터 가져오기 + 로컬/OpenShift Local 경로 정리
## 3. S3 입력 데이터
| 항목 | 값 |
|---|---|
| bucket | edu-ai-lake |
| key | users/kim-juil/clean/customers/customers_clean_20260606_v2.csv |
| S3 URI | s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv |
| 데이터 상태 | clean |
| 데이터셋 | customers |
| 버전 | 20260606_v2 |
## 4. 로컬 저장 경로
| 항목 | 값 |
|---|---|
| 로컬 상대 경로 | data/clean/customers_clean_20260606_v2.csv |
| 로컬 절대 경로 | /home/soldesk/week2-reproducibility/data/clean/customers_clean_20260606_v2.csv |
| 파일 존재 여부 | True |
| 파일 크기 bytes | 1595 |
## 5. 다운로드 방식
| 방식 | 설명 |
|---|---|
| AWS CLI | `aws s3 cp` 명령으로 다운로드 |
| boto3 | `boto3.client("s3").download_file()` 함수로 다운로드 |
## 6. pandas 읽기 확인
| 항목 | 값 |
|---|---|
| read_csv 성공 | True |
| shape | [9, 29] |
| columns | ['customer_id', 'age', 'monthly_fee', 'usage_days', 'support_calls', 'gender_standard', 'contract_type_standard', 'signup_date', 'last_login_date', 'signup_year', 'signup_month', 'last_login_dayofweek', 'last_login_day_name', 'days_since_signup', 'days_since_last_login', 'age_was_missing', 'monthly_fee_was_missing', 'gender_was_missing', 'contract_type_was_missing', 'monthly_fee_outlier', 'support_calls_outlier', 'is_high_fee', 'is_short_user', 'has_many_support_calls', 'usage_group', 'is_long_contract', 'churn', 'gender', 'contract_type'] |
## 7. OpenShift Local 연결
이번 교시에서는 OpenShift Local에 앱을 배포하지 않았다.
하지만 같은 프로젝트 구조,
같은 `.env.example`,
같은 `src/s3_utils.py`,
같은 S3 clean key를 사용하면
OpenShift Local 환경에서도 동일한 방식으로 데이터를 가져올 수 있다.
## 8. g4dn.xlarge 연결
이번 교시에서는 g4dn.xlarge를 사용하지 않았다.
S3 다운로드와 pandas 데이터 읽기에는 GPU가 필요하지 않다.
이후 GPU 실습 주차에서는 Day 5에서 만든 feature/log/artifact 구조를 그대로 사용한다.
## 9. 다음 교시 연결
3교시에서는 내려받은 clean 데이터를 바로 모델링하지 않고,
컬럼, 타입, 결측치, target, row 수를 먼저 검증한다.
