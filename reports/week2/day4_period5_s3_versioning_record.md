# 2주차 Day 4 5교시 실습 기록지

## 작성자

- author: student

## 1. 오늘 주제

S3 Versioning 개념 + 덮어쓰기 실습

## 2. Versioning 개념

- S3 Versioning이란?
- 같은 S3 Key에 객체를 다시 업로드해도 이전 객체를 바로 없애지 않고, 여러 버전으로 보관할 수 있게 하는 기능이다.

## 3. 버킷 Versioning 상태

| 항목 | 값 |
|---|---|
| 버킷 이름 | edu-ai-lake |
| Versioning 상태 | 확인 필요 |
| 확인 명령 | `aws s3api get-bucket-versioning --bucket edu-ai-lake` |

## 4. 실습 대상

| 항목 | 값 |
|---|---|
| 실습 대상 Prefix | users/student/clean/customers/versioning-test/ |
| 실습 대상 Key | users/student/clean/customers/versioning-test/customers_clean_versioning_test_same_key.csv |
| raw 데이터 사용 여부 | 사용하지 않음 |
| clean 테스트 객체 사용 여부 | 사용 |

## 5. 업로드 파일

| 구분 | 로컬 파일 | S3 Key |
|---|---|---|
| v1 | tmp/versioning-test/customers_clean_versioning_test_v1.csv | users/student/clean/customers/versioning-test/customers_clean_versioning_test_same_key.csv |
| v2 | tmp/versioning-test/customers_clean_versioning_test_v2.csv | users/student/clean/customers/versioning-test/customers_clean_versioning_test_same_key.csv |

## 6. VersionId 기록

| 구분 | VersionId | IsLatest |
|---|---|---|
| 최신 버전 | 3iXQrUi9ABymAGpru_o.ge.sU.Ds5.7c | True |
| 이전 버전 | LZhs08WF7SryWWKS3liDFWUtBgOne8ew | False |

## 7. 이전 버전 다운로드 결과

| 항목 | 결과 |
|---|---|
| 다운로드 파일 | tmp/versioning-test/download_previous.csv |
| marker 값 | v1_first_upload: 9개 |
| 이전 버전 확인 성공 여부 | 확인 필요 |

## 8. 복구 개념

- 이전 버전을 복구하려면 어떤 값이 필요한가?
- 복구하려면 보통 복구 대상 객체의 `Key`와 이전 버전의 `VersionId`가 필요하다.
- 특정 VersionId를 다운로드하거나, 이전 버전을 다시 같은 Key로 업로드해서 최신 버전으로 만들 수 있다.

## 9. Delete Marker 개념

- Versioning 상태에서 삭제하면 어떤 개념이 생길 수 있는가?
- Versioning이 켜진 버킷에서 객체를 일반 삭제하면 실제 이전 버전이 바로 지워지지 않고 Delete Marker가 최신 버전으로 생길 수 있다.
- Delete Marker는 파일 내용이 아니라 삭제된 것처럼 보이게 하는 표시용 버전이다.

## 10. 운영 원칙

- Versioning이 파일명 규칙을 대체할 수 있는가?
  - 대체할 수 없다. Versioning은 복구 보조 기능이고, 파일명 규칙은 사람이 데이터 상태를 이해하기 위한 운영 기준이다.
- Versioning이 raw 덮어쓰기를 허용하는 근거가 되는가?
  - 아니다. raw 데이터는 원본이므로 같은 Key로 덮어쓰지 않는 것이 원칙이다.
- 좋은 운영 원칙은 무엇인가?
  - raw, clean, feature, log, artifact를 Prefix로 분리한다.
  - 파일명에 데이터셋, 상태, 날짜, 버전을 포함한다.
  - Versioning은 실수 복구용 보조 장치로 사용한다.
  - 중요한 삭제 작업 전에는 VersionId와 Delete Marker를 확인한다.

## 11. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서 Versioning 원칙이 필요한 이유는?
- OpenShift에서 실행되는 Pod도 같은 S3 Prefix에 접근할 수 있으므로, 잘못된 업로드나 덮어쓰기 실수를 줄이기 위해 Versioning과 파일명 규칙이 필요하다.

## 12. g4dn 연결

- g4dn GPU 실습 결과에 Versioning이 필요한 이유는?
- GPU 실습 결과는 모델 파일, 추론 결과, 로그처럼 다시 만들기 어렵거나 비용이 드는 산출물이 포함될 수 있으므로 Versioning과 명확한 파일명 규칙이 필요하다.

## 13. 생성한 산출물

| 산출물 | 경로 |
|---|---|
| 버전 목록 원본 JSON | outputs/day4_s3_versioning_versions_raw.json |
| VersionId 요약 JSON | outputs/day4_s3_versioning_version_ids.json |
| Versioning 기록 JSON | outputs/day4_s3_versioning_record.json |
| Versioning 기록 Markdown | outputs/day4_s3_versioning_record.md |

## 14. 오늘 이해한 점

-

## 15. 다음 교시에서 할 일

S3 Lifecycle 개념 + 보관 정책 설계
