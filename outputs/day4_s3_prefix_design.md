# Day 4 S3 Prefix 설계안
## 1. 작성자
- author: student
## 2. 버킷 이름
- bucket: edu-ai-lake
## 3. 기본 전략
- strategy: single_bucket_with_user_prefix
- 설명: 버킷 1개 안에서 common/과 users/<author>/ Prefix를 분리한다.
## 4. 공통 Prefix 구조
- common/raw/customers/
- common/reference/week2/
## 5. 개인 Prefix 구조
- users/student/raw/customers/
- users/student/clean/customers/
- users/student/feature/customers/
- users/student/notebook/week2/
- users/student/artifact/week2/
- users/student/log/week2/
- users/student/archive/
## 6. 고객 데이터 저장 위치
- raw: users/student/raw/customers/
- clean: users/student/clean/customers/
- feature: users/student/feature/customers/
## 7. 산출물 저장 위치
- notebook: users/student/notebook/week2/
- artifact: users/student/artifact/week2/
- log: users/student/log/week2/
## 8. raw 데이터 원칙
- raw 데이터는 원본이다.
- raw 데이터는 수정하지 않는다.
- raw 데이터는 덮어쓰지 않는다.
- raw 데이터는 쉽게 삭제하지 않는다.
- 변경이 필요하면 새 파일명과 새 버전으로 업로드한다.
## 9. clean 데이터 원칙
- clean 데이터는 전처리 완료 데이터이다.
- 처리 기준은 리포트 또는 run_info에 기록한다.
- 파일명에 날짜와 버전을 포함한다.
- raw와 같은 위치에 섞지 않는다.
## 10. feature 데이터 원칙
- feature 데이터는 모델 학습용 특징 데이터이다.
- train/test split 기준을 기록한다.
- 데이터 누수 위험을 점검한다.
- feature_version을 기록한다.
## 11. log / artifact 원칙
- run_info.json은 log/에 저장한다.
- 업로드 기록 JSON은 log/에 저장한다.
- 리포트와 모델 파일은 artifact/에 저장한다.
- 제출 산출물은 쉽게 삭제하지 않는다.
## 12. OpenShift 연결
- OpenShift Local 또는 Developer Sandbox에서도 같은 S3 Prefix를 사용한다.
- 로컬 경로가 아니라 S3 Prefix 기준으로 데이터를 찾을 수 있어야 한다.
- OpenShift에서는 S3 접근 정보를 Secret 또는 환경 변수로 주입할 수 있다.
## 13. g4dn 연결
- Day 4에서는 g4dn.xlarge를 사용하지 않는다.
- GPU 실습 주차에서는 g4dn에서 생성한 결과물을 같은 users/student/artifact/ 또는 log/ Prefix에 저장한다.
## 14. 3교시 업로드 대상
- data/raw/customers_raw.csv → users/student/raw/customers/
- data/clean/customers_clean_20260606_v2.csv → users/student/clean/customers/
- outputs/run_info.json → users/student/log/week2/
