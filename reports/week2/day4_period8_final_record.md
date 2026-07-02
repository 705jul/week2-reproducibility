# 2주차 Day 4 8교시 최종 실습 기록지

## 작성자

- author: kim-juil

## 1. 오늘 주제

Day 4 산출물 정리 + Day 5 예고

## 2. 사용한 S3 버킷

- bucket: edu-ai-lake

## 3. 개인 author

- author: kim-juil

## 4. 사용한 Prefix

| 구분 | Prefix |
|---|---|
| raw | users/kim-juil/raw/customers/ |
| clean | users/kim-juil/clean/customers/ |
| feature | users/kim-juil/feature/customers/ |
| notebook | users/kim-juil/notebook/week2/ |
| artifact | users/kim-juil/artifact/week2/ |
| log | users/kim-juil/log/week2/ |
| archive | users/kim-juil/archive/ |
| tmp | users/kim-juil/tmp/ |

## 5. 업로드한 핵심 파일

| 구분 | 로컬 파일 | S3 URI |
|---|---|---|
| raw | data/raw/customers_raw.csv | s3://edu-ai-lake/users/kim-juil/raw/customers/customers_raw_20260605_v1.csv |
| clean | data/clean/customers_clean_20260606_v2.csv | s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv |
| run_info | outputs/run_info.json | s3://edu-ai-lake/users/kim-juil/log/week2/run_info_20260606_kim-juil.json |
| upload record | outputs/day4_s3_upload_record.md | s3://edu-ai-lake/users/kim-juil/log/week2/day4_s3_upload_record_kim-juil.md |
| final summary | outputs/day4_final_summary.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_final_summary_kim-juil.md |

## 6. 작성한 문서

| 문서 | 로컬 경로 | S3 업로드 위치 |
|---|---|---|
| S3 Prefix 설계안 | reports/week2/day4_period2_s3_prefix_design_record.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_period2_s3_prefix_design_record_kim-juil.md |
| S3 업로드 기록 | outputs/day4_s3_upload_record.md | s3://edu-ai-lake/users/kim-juil/log/week2/day4_s3_upload_record_kim-juil.md |
| 파일명 규칙 | outputs/day4_s3_file_naming_rules.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_s3_file_naming_rules_kim-juil.md |
| 데이터 적재 규칙 | outputs/day4_s3_data_loading_rules.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_s3_data_loading_rules_kim-juil.md |
| Versioning 기록 | outputs/day4_s3_versioning_record.md | s3://edu-ai-lake/users/kim-juil/log/week2/day4_s3_versioning_record_kim-juil.md |
| Lifecycle 설계 | outputs/day4_s3_lifecycle_design.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_s3_lifecycle_design_kim-juil.md |
| IAM 운영 규칙 | outputs/day4_s3_iam_operation_rules.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_s3_iam_operation_rules_kim-juil.md |
| Day 4 최종 요약 | outputs/day4_final_summary.md | s3://edu-ai-lake/users/kim-juil/artifact/week2/day4_final_summary_kim-juil.md |

## 7. Versioning 확인

| 항목 | 값 |
|---|---|
| 실습 대상 Key | users/kim-juil/clean/customers/versioning-test/customers_clean_versioning_test_same_key.csv |
| 최신 VersionId | 3iXQrUi9ABymAGpru_o.ge.sU.Ds5.7c |
| 이전 VersionId | LZhs08WF7SryWWKS3liDFWUtBgOne8ew |
| 이전 버전 다운로드 확인 여부 | 확인 필요 |

## 8. Lifecycle 설계 요약

| Prefix | 보관 정책 |
|---|---|
| raw | 원본 데이터이므로 장기 보관하고 자동 삭제를 제한한다. |
| clean | 전처리 완료 데이터이므로 버전과 처리 기준을 함께 보관한다. |
| feature | 모델 학습 재현에 필요하므로 모델 버전과 연결해 보관한다. |
| log | 실행 조건 추적용이므로 삭제를 제한하고 장기 보관을 검토한다. |
| artifact | 리포트, 모델 파일, 최종 산출물이므로 삭제 전 승인 기준이 필요하다. |
| tmp | 실습용 임시 파일만 저장하고 짧은 기간 후 정리 후보로 둔다. |

## 9. IAM 최소 권한 요약

| 항목 | 기준 |
|---|---|
| 학생 개인 권한 범위 | 본인 users/kim-juil/ Prefix 중심으로 제한한다. |
| raw 삭제 권한 | 기본적으로 허용하지 않는다. |
| log 삭제 권한 | 기본적으로 제한한다. |
| artifact 삭제 권한 | 최종 산출물 삭제는 제한한다. |
| tmp 삭제 권한 | 실습용 tmp Prefix에 한해 제한적으로 허용할 수 있다. |
| Lifecycle 설정 변경 | 학생 개인에게 허용하지 않는다. |
| Versioning 설정 변경 | 학생 개인에게 허용하지 않는다. |

## 10. Day 5 준비 상태

| 항목 | 값 |
|---|---|
| Day 5 입력 clean S3 URI | s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv |
| clean 데이터 상태 | 로컬 파일 확인됨: data/from_s3/customers_clean_20260606_v2.csv |
| baseline 준비 가능 여부 | 가능 |
| 추가로 확인할 점 | S3에서 받은 clean 데이터의 shape, columns, target 컬럼, feature 후보 컬럼을 확인한다. |

## 11. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서 같은 S3 Prefix를 어떻게 사용할 것인가?
- OpenShift에서 실행되는 애플리케이션은 S3_BUCKET, S3_CLEAN_PREFIX, S3_LOG_PREFIX, S3_ARTIFACT_PREFIX 같은 값을 환경 변수 또는 ConfigMap으로 주입받을 수 있다.
- AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 관리한다.
- Pod가 모든 S3 경로에 접근하지 않도록 본인 Prefix 중심의 최소 권한을 적용한다.

## 12. g4dn 연결

- g4dn GPU 실습 결과는 어느 Prefix에 저장할 것인가?
- GPU 실습 결과, 모델 파일, 추론 결과, 실행 로그는 artifact와 log Prefix로 분리해서 저장한다.
- 예시 저장 위치는 다음과 같다.
  - users/kim-juil/artifact/week7/
  - users/kim-juil/log/week7/
- raw 원본 데이터는 GPU 실습 중에도 덮어쓰지 않는다.

## 13. 오늘 이해한 점

- S3는 단순 파일 저장소가 아니라 AI 실험 데이터 자산 저장소이다.
- Prefix는 데이터의 위치를 나누는 운영 기준이다.
- 파일명 규칙은 데이터 상태와 버전을 사람이 이해할 수 있게 해준다.
- Versioning은 실수 복구를 돕지만 파일명 규칙을 대체하지 않는다.
- Lifecycle은 비용과 보관 기간을 관리하지만 raw, log, artifact에는 조심해서 적용해야 한다.
- IAM 최소 권한은 사고를 예방하는 기본 원칙이다.

## 14. 다음 Day 5에서 할 일

S3 clean 데이터 읽기 + baseline 준비
