# Day 4 S3 데이터 레이크 구조 초안
## 1. 작성자
- author: student
## 2. Day 1~3 결과 연결
### Day 1
- 데이터 관찰
- raw 데이터 확인
- data/raw/customers_raw.csv 생성
### Day 2
- clean 데이터 생성
- 전처리 리포트 작성
- data/clean/customers_clean_20260606_v2.csv 생성
### Day 3
- 재현 가능한 실행 환경 구성
- requirements.txt 작성
- .env.example 작성
- src/ 구조 작성
- outputs/run_info.json 작성
## 3. S3를 사용하는 이유
- 개인 PC에만 있는 데이터를 기준 저장소로 옮기기 위해
- raw와 clean을 분리하기 위해
- 데이터 버전을 관리하기 위해
- 실행 로그와 산출물을 함께 보관하기 위해
- 오래된 데이터를 Lifecycle로 관리하기 위해
- OpenShift Local / Developer Sandbox / g4dn에서도 같은 데이터 기준을 사용하기 위해
## 4. Prefix 초안
- common/
- users/<author>/
- raw/
- clean/
- feature/
- notebook/
- artifact/
- log/
- archive/
## 5. raw 데이터 원칙
- 원본 데이터는 수정하지 않는다.
- 원본 데이터는 덮어쓰지 않는다.
- 원본 데이터는 쉽게 삭제하지 않는다.
- 변경이 필요하면 새 파일명과 새 버전으로 업로드한다.
## 6. clean 데이터 원칙
- 전처리 완료 데이터를 저장한다.
- 처리 기준을 리포트에 기록한다.
- 파일명에 날짜와 버전을 포함한다.
- raw와 같은 위치에 섞지 않는다.
## 7. feature 데이터 원칙
- 모델 학습용 특징 데이터를 저장한다.
- train/test split 기준을 기록한다.
- 데이터 누수 위험을 점검한다.
- feature_version을 기록한다.
## 8. log / artifact 원칙
- run_info.json은 log/에 저장한다.
- 리포트와 모델 파일은 artifact/에 저장한다.
- 제출 산출물은 쉽게 삭제하지 않는다.
## 9. 아직 결정해야 할 것
- 버킷 이름:
- 개인 author:
- 개인 Prefix:
- raw 보관 기간:
- clean 보관 기간:
- feature 보관 기간:
- 삭제 권한 기준:
- Versioning 확인 방법:
- Lifecycle 전환 기준:
