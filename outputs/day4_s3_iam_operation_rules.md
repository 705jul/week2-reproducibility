# Day 4 S3 IAM 최소 권한 + 개인 운영 규칙
## 1. 작성자
- author: student
## 2. 실습 리전
- region: ap-northeast-2
## 3. 사용 버킷
- bucket: edu-ai-lake
## 4. 개인 Prefix
- user_prefix: users/student/
## 5. IAM 최소 권한 원칙
필요한 사람에게,
필요한 Prefix에 대해서,
필요한 Action만 허용한다.
모든 학생에게 S3 FullAccess 또는 AdministratorAccess를 주지 않는다.
## 6. 개인 Prefix 구조
| Prefix | 역할 |
|---|---|
| users/student/raw/customers/ | 원본 고객 데이터 |
| users/student/clean/customers/ | 전처리 완료 고객 데이터 |
| users/student/feature/customers/ | 모델 학습용 feature 데이터 |
| users/student/notebook/week2/ | Week 2 Notebook |
| users/student/artifact/week2/ | Week 2 리포트와 산출물 |
| users/student/log/week2/ | Week 2 실행 기록과 업로드 기록 |
| users/student/archive/ | 장기 보관 데이터 |
| users/student/tmp/ | 임시 파일 |
## 7. 학생 개인 권한 원칙
- 본인 Prefix 중심으로 작업한다.
- 다른 개인 Prefix에 쓰기 권한을 갖지 않는다.
- raw 데이터는 읽을 수 있지만 삭제하지 않는다.
- clean 데이터는 본인 Prefix에 업로드할 수 있다.
- feature 데이터는 본인 Prefix에 업로드할 수 있다.
- log는 쓰고 읽을 수 있지만 삭제하지 않는다.
- artifact는 업로드할 수 있지만 최종 산출물은 삭제하지 않는다.
- tmp는 본인 Prefix 안에서 정리할 수 있다.
- Versioning 설정을 바꾸지 않는다.
- Lifecycle 설정을 바꾸지 않는다.
- 버킷 정책을 바꾸지 않는다.
## 8. 강사 또는 관리자 권한 원칙
- 교육용 버킷 구조를 관리한다.
- Versioning 상태를 확인하고 필요 시 설정한다.
- Lifecycle 정책을 검토하고 필요 시 적용한다.
- 학생 산출물을 조회한다.
- raw 삭제 또는 복구는 승인 절차에 따라 수행한다.
- 사고 발생 시 CloudTrail과 S3 log를 확인한다.
## 9. 파이프라인 권한 원칙
- 정해진 입력 Prefix를 읽는다.
- 정해진 출력 Prefix에 결과를 쓴다.
- 실행 로그를 log Prefix에 남긴다.
- raw 데이터를 삭제하지 않는다.
- Lifecycle이나 Versioning 설정을 변경하지 않는다.
## 10. 감사자 권한 원칙
- log와 감사 기록을 조회한다.
- 데이터를 업로드하지 않는다.
- 데이터를 삭제하지 않는다.
- 권한 변경을 수행하지 않는다.
## 11. Prefix별 권한 설계
| Prefix | Get | Put | Delete | 비고 |
|---|---|---|---|---|
| raw/customers | 허용 | 제한 | 금지 | 원본 보호 |
| clean/customers | 허용 | 허용 | 제한 | 전처리 결과 |
| feature/customers | 허용 | 허용 | 제한 | 모델 입력 |
| notebook/week2 | 허용 | 허용 | 제한 | 실습 기록 |
| artifact/week2 | 허용 | 허용 | 제한 | 평가 산출물 |
| log/week2 | 허용 | 허용 | 금지 | 실행 추적 |
| archive | 허용 | 제한 | 승인 필요 | 장기 보관 |
| tmp | 허용 | 허용 | 허용 | 임시 파일 |
## 12. 명시적으로 제한해야 할 작업
- raw DeleteObject
- raw DeleteObjectVersion
- log DeleteObject
- artifact 최종 산출물 DeleteObject
- PutBucketVersioning
- PutLifecycleConfiguration
- PutBucketPolicy
- DeleteBucket
- 다른 개인 Prefix PutObject
- 다른 개인 Prefix DeleteObject
## 13. OpenShift 연결
OpenShift Local 또는 Developer Sandbox에서는 S3_BUCKET, S3_USER_PREFIX, S3_CLEAN_PREFIX, S3_LOG_PREFIX를 환경 변수 또는 ConfigMap으로 주입한다.
AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 관리한다.
OpenShift에서 실행되는 Notebook, Job, FastAPI도 최소 권한 원칙을 따른다.
## 14. g4dn 연결
Day 4에서는 g4dn.xlarge를 사용하지 않는다.
GPU 실습 주차에서는 g4dn 인스턴스에 필요한 S3 Prefix 권한만 부여한다.
가능하면 Access Key 파일 저장보다 EC2 IAM Role을 사용한다.
g4dn 결과는 artifact/week7/과 log/week7/에 저장한다.
## 15. 사고 예방 규칙
- raw 삭제는 관리자 승인 없이는 수행하지 않는다.
- log 삭제는 수행하지 않는다.
- artifact 최종 산출물 삭제는 승인 후 수행한다.
- Lifecycle 정책은 학생 개인이 임의 변경하지 않는다.
- Versioning 설정은 학생 개인이 임의 변경하지 않는다.
- Access Key와 Secret Key는 코드, README, Notebook, Git 저장소에 남기지 않는다.
- 업로드 후 S3 URI와 author를 기록한다.
- 본인 Prefix가 맞는지 업로드 전에 확인한다.
## 16. 다음 교시 연결
8교시에서는 Day 4 전체 산출물을 정리하고,
Day 5에서 S3 clean 데이터를 읽어 baseline 준비로 연결한다.
