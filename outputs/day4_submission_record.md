# 2주차 Day 4 제출 확인 기록
## 1. 작성자
- author: student
## 2. 버킷
- bucket: edu-ai-lake
## 3. 개인 Prefix
| 구분 | Prefix |
|---|---|
| raw | users/student/raw/customers/ |
| clean | users/student/clean/customers/ |
| feature | users/student/feature/customers/ |
| notebook | users/student/notebook/week2/ |
| artifact | users/student/artifact/week2/ |
| log | users/student/log/week2/ |
| archive | users/student/archive/ |
## 4. 업로드한 파일 기록
| 구분 | 로컬 파일 | S3 위치 |
|---|---|---|
| raw | data/raw/customers_raw.csv | s3://edu-ai-lake/users/student/raw/customers/ |
| clean | data/clean/customers_clean_20260606_v2.csv | s3://edu-ai-lake/users/student/clean/customers/ |
| run_info | outputs/run_info.json | s3://edu-ai-lake/users/student/log/week2/ |
| upload record | outputs/day4_s3_upload_record.json | s3://edu-ai-lake/users/student/log/week2/ |
| lifecycle design | outputs/day4_s3_lifecycle_design.md | s3://edu-ai-lake/users/student/artifact/week2/ |
| iam rules | outputs/day4_s3_iam_operation_rules.md | s3://edu-ai-lake/users/student/artifact/week2/ |
## 5. 작성한 주요 문서
| 문서 | 로컬 경로 |
|---|---|
| S3 데이터 레이크 구조 초안 | outputs/day4_s3_data_lake_draft.md |
| S3 Prefix 설계안 | outputs/day4_s3_prefix_design.md |
| S3 Prefix 설계 JSON | outputs/day4_s3_prefix_design.json |
| S3 업로드 기록 | outputs/day4_s3_upload_record.md |
| S3 파일명 규칙 | outputs/day4_s3_file_naming_rules.md |
| S3 데이터 적재 규칙 | outputs/day4_s3_data_loading_rules.md |
| S3 Versioning 기록 | outputs/day4_s3_versioning_record.md |
| S3 Lifecycle 설계 | outputs/day4_s3_lifecycle_design.md |
| S3 IAM 운영 규칙 | outputs/day4_s3_iam_operation_rules.md |
| 개인 권한 매트릭스 | outputs/day4_s3_personal_permission_matrix.md |
| Day 4 최종 요약 | outputs/day4_final_summary.md |
## 6. Versioning 확인 기록
| 항목 | 기록 |
|---|---|
| Versioning 실습 대상 | users/student/clean/customers/versioning-test/ |
| 최신 VersionId 기록 | outputs/day4_s3_versioning_version_ids.json |
| 버전 목록 원본 | outputs/day4_s3_versioning_versions_raw.json |
| 이전 버전 다운로드 확인 | tmp/versioning-test/download_previous.csv |
## 7. Lifecycle 설계 요약
| Prefix | 보관 기준 |
|---|---|
| raw | 장기 보관, 자동 삭제 금지 |
| clean | 중기/장기 보관 |
| feature | 재생성 가능성 확인 후 정리 후보 |
| log | 추적 기간 보관 |
| artifact | 평가/제출 기간 보관 |
| tmp | 짧은 기간 후 정리 후보 |
## 8. IAM 최소 권한 요약
| 항목 | 기준 |
|---|---|
| 학생 개인 범위 | users/student/ |
| raw 삭제 | 제한 |
| log 삭제 | 제한 |
| artifact 최종 산출물 삭제 | 제한 |
| tmp 삭제 | 본인 tmp Prefix 안에서 허용 가능 |
| Versioning 설정 변경 | 학생 개인에게 불필요 |
| Lifecycle 설정 변경 | 학생 개인에게 불필요 |
| 다른 개인 Prefix 쓰기 | 허용하지 않음 |
## 9. Day 5 준비 상태
| 항목 | 값 |
|---|---|
| Day 5 입력 데이터 | s3://edu-ai-lake/users/student/clean/customers/customers_clean_20260606_v2.csv |
| 입력 데이터 상태 | clean |
| 다음 실습 | S3 clean 데이터 읽기 + baseline 준비 |
| 중심 환경 | 개인 로컬 PC WSL2 |
| OpenShift | 같은 S3 URI 사용 구조로 연결 |
| g4dn | Day 4에서는 미사용, GPU 주차에서 연결 |
## 10. 오늘 배운 핵심
S3는 단순 파일 저장소가 아니라 AI 실험 데이터 자산의 기준 저장소다.
raw, clean, feature, log, artifact는 역할이 다르며 Prefix도 분리해야 한다.
파일명에는 dataset, stage, 날짜, 버전, 확장자가 드러나야 한다.
Versioning은 안전망이고, Lifecycle은 보관 정책이며, IAM 최소 권한은 사고 예방 장치다.
Day 5에서는 S3 clean 데이터를 다시 읽어 baseline 준비로 연결한다.
