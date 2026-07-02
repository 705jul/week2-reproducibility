# 2주차 Day 4 최종 요약

## 1. 작성자

- author: student

## 2. 실습 리전

- region: ap-northeast-2

## 3. 사용한 S3 버킷

- bucket: edu-ai-lake

## 4. Day 4 주제

S3 데이터 적재 / 버전관리 / 수명주기

S3는 Simple Storage Service의 약자이며, AWS에서 객체 파일을 저장하는 스토리지 서비스이다.

## 5. Day 4 핵심 메시지

Day 4의 목표는 S3에 파일을 올리는 것에서 끝나지 않는다.

S3 Prefix, 업로드 기록, 파일명 규칙, Versioning, Lifecycle, IAM 최소 권한을 함께 정리해야  
운영 가능한 AI 실험 데이터 자산 구조가 된다.

IAM은 Identity and Access Management의 약자이며, AWS에서 사용자와 권한을 관리하는 서비스이다.

## 6. 개인 Prefix 구조

| 구분 | Prefix |
|---|---|
| user | users/student/ |
| raw | users/student/raw/customers/ |
| clean | users/student/clean/customers/ |
| feature | users/student/feature/customers/ |
| notebook | users/student/notebook/week2/ |
| artifact | users/student/artifact/week2/ |
| log | users/student/log/week2/ |
| archive | users/student/archive/ |
| tmp | users/student/tmp/ |

## 7. 업로드한 핵심 데이터

| 구분 | S3 URI |
|---|---|
| raw | s3://edu-ai-lake/users/student/raw/customers/customers_raw_20260605_v1.csv |
| clean | s3://edu-ai-lake/users/student/clean/customers/customers_clean_20260606_v2.csv |
| run_info | s3://edu-ai-lake/users/student/log/week2/run_info_20260606_student.json |
| artifact | s3://edu-ai-lake/users/student/artifact/week2/ |

## 8. 파일명 규칙

기본 형식:

```text
{dataset}_{stage}_{yyyymmdd}_v{version}.{ext}
```

예시:

```text
customers_raw_20260605_v1.csv
customers_clean_20260606_v2.csv
customers_feature_20260607_v1.parquet
run_info_week2_day4_20260606_v1.json
```

좋은 파일명은 파일을 열어보지 않아도 데이터셋, 상태, 생성일, 버전을 알 수 있어야 한다.

## 9. Versioning 요약

S3 Versioning은 같은 객체 Key에 여러 버전을 보존할 수 있게 해주는 안전망이다.

하지만 Versioning은 파일명 규칙을 대체하지 않는다.

Versioning이 있다고 raw 데이터를 덮어써도 되는 것도 아니다.

운영 원칙은 다음과 같다.

- raw 데이터는 같은 Key로 덮어쓰지 않는다.
- clean 데이터는 날짜와 버전을 포함한 파일명으로 관리한다.
- 이전 버전 복구에는 Key와 VersionId가 중요하다.
- Delete Marker는 삭제된 것처럼 보이게 하는 표시용 버전이다.

## 10. Lifecycle 요약

Lifecycle은 오래된 객체를 다른 스토리지 클래스로 전환하거나 일정 기간 후 만료 처리하는 보관 정책이다.

raw는 원본 재현 기준이므로 자동 삭제 정책을 매우 조심해야 한다.

tmp와 versioning-test 같은 실습용 Prefix는 짧은 기간 후 정리 후보가 될 수 있다.

Lifecycle 운영 원칙은 다음과 같다.

- raw Prefix에는 위험한 자동 삭제를 걸지 않는다.
- log Prefix는 실행 추적에 필요하므로 삭제에 주의한다.
- artifact Prefix는 결과 산출물 보관용이므로 삭제 제한이 필요하다.
- tmp Prefix는 실습용 임시 파일 정리 후보가 될 수 있다.
- versioning-test Prefix는 이전 버전 정리 실습 후보가 될 수 있다.

## 11. IAM 최소 권한 요약

필요한 사람에게, 필요한 Prefix에 대해서, 필요한 Action만 허용한다.

학생 개인은 본인 users/student/ Prefix 중심으로 작업한다.

권한 운영 원칙은 다음과 같다.

- raw 삭제는 제한한다.
- log 삭제는 제한한다.
- artifact 최종 산출물 삭제는 제한한다.
- 다른 개인의 Prefix 접근은 제한한다.
- Versioning과 Lifecycle 설정 변경은 학생 개인이 임의로 수행하지 않는다.
- PutBucketPolicy, PutBucketVersioning, PutLifecycleConfiguration 같은 버킷 전체 설정 권한은 관리자 중심으로 관리한다.

## 12. OpenShift Local / Developer Sandbox 연결

Day 4에서는 OpenShift 앱 배포를 하지 않았다.

하지만 OpenShift Local 또는 Developer Sandbox에서도 같은 S3 Prefix를 사용할 수 있어야 한다.

OpenShift에서는 다음 값을 환경 변수 또는 ConfigMap으로 주입할 수 있다.

```text
S3_BUCKET=edu-ai-lake
S3_CLEAN_PREFIX=users/student/clean/customers/
S3_LOG_PREFIX=users/student/log/week2/
S3_ARTIFACT_PREFIX=users/student/artifact/week2/
```

AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 관리한다.

OpenShift에서 실행되는 애플리케이션도 raw, clean, feature, log, artifact Prefix를 구분해서 사용해야 한다.

## 13. g4dn.xlarge 연결

Day 4에서는 g4dn.xlarge를 사용하지 않았다.

S3 데이터 운영 실습에는 GPU가 필요하지 않기 때문이다.

이후 GPU 실습 주차에서는 g4dn에서 생성한 GPU 결과, 모델 파일, 실행 로그를 같은 artifact/log Prefix 체계로 저장한다.

예시 저장 위치는 다음과 같다.

```text
users/student/artifact/week7/
users/student/log/week7/
```

g4dn 실습 결과도 파일명에 데이터셋, stage, 날짜, 버전을 포함하는 것이 좋다.

## 14. Day 5 준비

Day 5에서는 아래 clean 데이터를 다시 읽어 baseline 준비를 시작한다.

```text
s3://edu-ai-lake/users/student/clean/customers/customers_clean_20260606_v2.csv
```

Day 5에서 할 일:

- S3 clean 데이터 읽기
- 데이터 shape 확인
- 컬럼과 타입 확인
- target 컬럼 확인
- feature 후보 컬럼 확인
- train/test split 준비
- baseline 모델 준비 기록 작성

## 15. 오늘 이해한 점

S3는 단순 파일 저장소가 아니다.

AI 실험에서 S3는 raw, clean, feature, notebook, artifact, log, archive를 체계적으로 관리하는 데이터 자산 저장소다.

좋은 데이터 운영은 업로드 명령어가 아니라 Prefix, 파일명, 버전, 보관 정책, 권한 규칙에서 시작한다.

## 16. Day 4 생성 산출물 요약

| 산출물 | 경로 |
|---|---|
| S3 업로드 기록 Markdown | outputs/day4_s3_upload_record.md |
| 파일명 규칙 Markdown | outputs/day4_s3_file_naming_rules.md |
| 데이터 적재 규칙 Markdown | outputs/day4_s3_data_loading_rules.md |
| 데이터 적재 규칙 JSON | outputs/day4_s3_data_loading_rules.json |
| Versioning 기록 Markdown | outputs/day4_s3_versioning_record.md |
| Versioning 기록 JSON | outputs/day4_s3_versioning_record.json |
| Lifecycle 설계 Markdown | outputs/day4_s3_lifecycle_design.md |
| Lifecycle 설계 JSON | outputs/day4_s3_lifecycle_design.json |
| Lifecycle tmp 정책 예시 JSON | outputs/day4_s3_lifecycle_tmp_policy_example.json |
| IAM 운영 규칙 Markdown | outputs/day4_s3_iam_operation_rules.md |
| IAM 운영 규칙 JSON | outputs/day4_s3_iam_operation_rules.json |
| 개인 권한 매트릭스 | outputs/day4_s3_personal_permission_matrix.md |
| Day 4 최종 요약 Markdown | outputs/day4_final_summary.md |
