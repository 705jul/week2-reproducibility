# Day 4 5교시 S3 Versioning 실습 기록
## 1. 작성자
- author: student
## 2. 버킷
- bucket: edu-ai-lake
## 3. 오늘 주제
S3 Versioning 개념 + 덮어쓰기 실습
## 4. 핵심 개념
S3 Versioning은 같은 객체 Key에 여러 버전을 보존할 수 있게 해주는 기능이다.
Versioning은 덮어쓰기와 삭제 실수에 대비하는 안전망이다.
하지만 Versioning은 파일명 규칙을 대체하지 않는다.
raw 데이터 덮어쓰기도 권장하지 않는다.
## 5. 실습 대상
이번 실습은 raw 데이터가 아니라 clean 테스트 객체로 진행했다.
| 항목 | 값 |
|---|---|
| 실습 S3 Key | users/student/clean/customers/versioning-test/customers_clean_versioning_test_same_key.csv |
| 첫 번째 로컬 파일 | tmp/versioning-test/customers_clean_versioning_test_v1.csv |
| 두 번째 로컬 파일 | tmp/versioning-test/customers_clean_versioning_test_v2.csv |
| raw 덮어쓰기 실습 여부 | 하지 않음 |
## 6. 실습 흐름
1. 버킷 Versioning 상태 확인
2. v1 테스트 파일 생성
3. v1을 같은 S3 Key에 업로드
4. v2 테스트 파일 생성
5. v2를 같은 S3 Key에 다시 업로드
6. list-object-versions로 VersionId 확인
7. 최신 버전 다운로드 확인
8. 이전 VersionId 지정 다운로드 확인
9. 복구 개념 이해
10. Delete Marker 개념 이해
## 7. 생성된 로컬 기록 파일
| 파일 | 설명 |
|---|---|
| outputs/day4_s3_versioning_versions_raw.json | S3 버전 목록 원본 |
| outputs/day4_s3_versioning_version_ids.json | 최신/이전 VersionId 요약 |
| outputs/day4_s3_versioning_record.json | Versioning 실습 기록 |
| outputs/day4_s3_versioning_record.md | 사람이 읽는 Versioning 기록 |
## 8. 운영 원칙
- Versioning은 안전망이다.
- 파일명 규칙을 대체하지 않는다.
- raw 데이터는 덮어쓰지 않는다.
- raw 데이터는 새 파일명과 새 버전으로 업로드한다.
- clean 데이터도 가능하면 새 날짜와 새 버전으로 관리한다.
- 복구가 필요하면 VersionId를 확인한다.
- Versioning은 저장 비용을 증가시킬 수 있으므로 Lifecycle과 함께 설계한다.
## 9. OpenShift 연결
OpenShift Local 또는 Developer Sandbox에서 S3 객체를 읽고 쓰더라도 같은 Versioning 원칙을 따라야 한다.
ConfigMap으로 S3_BUCKET과 Prefix를 주입하고,
Secret으로 인증 정보를 관리하며,
실행 로그는 log/ Prefix에 남기는 것이 좋다.
## 10. g4dn 연결
Day 4에서는 g4dn.xlarge를 사용하지 않는다.
GPU 실습 주차에서는 모델 파일, GPU 실행 결과, CUDA 테스트 로그가 같은 S3 Versioning 원칙의 적용 대상이 될 수 있다.
예:
- users/student/artifact/week7/model_gpu_test_artifact_20260710_v1.pt
- users/student/log/week7/g4dn_run_info_20260710_v1.json
## 11. 다음 교시 연결
6교시에서는 오래된 객체와 이전 버전을 어떻게 보관하고 비용을 줄일지 S3 Lifecycle 개념과 보관 정책을 설계한다.
