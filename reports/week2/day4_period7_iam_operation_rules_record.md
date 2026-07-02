# 2주차 Day 4 7교시 실습 기록지

## 작성자

- author: student

## 1. 오늘 주제

IAM 최소 권한 + 개인 운영 규칙

## 2. IAM 최소 권한 정의

- 최소 권한이란?
- 사용자, 역할, 애플리케이션이 작업에 필요한 권한만 가지도록 제한하는 보안 원칙이다.
- 필요 이상으로 넓은 권한을 주지 않고, 필요한 Prefix와 필요한 작업만 허용한다.

## 3. 개인 Prefix

| 항목 | 값 |
|---|---|
| bucket | edu-ai-lake |
| author | student |
| user_prefix | users/student/ |

## 4. 학생 개인 권한

| Prefix | 허용할 작업 | 제한할 작업 |
|---|---|---|
| raw | 조회, 업로드 | 삭제, 덮어쓰기, 버전 삭제 |
| clean | 조회, 업로드 | 무분별한 삭제, 다른 사람 Prefix 접근 |
| feature | 조회, 업로드 | 무분별한 삭제, 다른 사람 Prefix 접근 |
| log | 조회, 업로드 | 삭제 |
| artifact | 조회, 업로드 | 최종 산출물 삭제 |
| tmp | 조회, 업로드, 실습용 삭제 | 다른 Prefix 삭제, Lifecycle 전체 설정 변경 |

## 5. raw 삭제 제한 이유

- raw 데이터는 원본 데이터이다.
- raw 데이터가 삭제되면 전처리 결과와 모델 학습 결과를 재현하기 어렵다.
- raw 데이터는 감사, 추적, 재실행의 기준이 된다.
- 따라서 학생 개인이 임의로 삭제하지 못하도록 제한하는 것이 안전하다.

## 6. log 삭제 제한 이유

- log는 실행 조건, 입력 파일, 출력 파일, seed, author, 업로드 기록을 추적하는 자료이다.
- log가 삭제되면 문제가 발생했을 때 원인을 추적하기 어렵다.
- 실험 결과가 달라졌을 때 비교 기준이 사라진다.
- 따라서 log는 쉽게 삭제하지 않는 것이 좋다.

## 7. artifact 삭제 제한 이유

- artifact는 리포트, 제출 산출물, 모델 파일, 결과 문서 등을 의미한다.
- 최종 제출물이나 모델 산출물이 삭제되면 교육 평가나 운영 확인에 문제가 생길 수 있다.
- 중요한 artifact는 삭제 전 승인 절차가 필요하다.

## 8. Versioning / Lifecycle 설정 권한

| 권한 | 학생 개인에게 허용 여부 | 이유 |
|---|---|---|
| PutBucketVersioning | 허용하지 않음 | 버킷 전체 Versioning 설정을 바꾸는 권한이므로 관리자 권한에 가깝다. |
| PutLifecycleConfiguration | 허용하지 않음 | Lifecycle 오설정 시 중요한 데이터가 자동 삭제될 수 있다. |
| PutBucketPolicy | 허용하지 않음 | 버킷 전체 접근 정책을 바꾸는 매우 민감한 권한이다. |
| DeleteObjectVersion | 기본적으로 허용하지 않음 | 특정 VersionId를 삭제하면 복구가 어려울 수 있다. |

## 9. 역할별 권한 설계

| 역할 | 주요 권한 | 제한 권한 |
|---|---|---|
| 학생 개인 | 본인 users/student/ Prefix 안에서 조회, 업로드, 실습용 tmp 삭제 | 버킷 정책 변경, Versioning 변경, Lifecycle 변경, 다른 사용자 Prefix 접근 |
| 강사/관리자 | 전체 실습 Prefix 조회, 정책 관리, 문제 복구 | 불필요한 운영 데이터 직접 삭제는 제한 |
| 파이프라인 | 지정된 Prefix에 자동 업로드, 로그 저장, 산출물 저장 | 버킷 전체 정책 변경, 다른 Prefix 삭제 |
| 감사자 | 로그와 산출물 조회 | 업로드, 삭제, 정책 변경 |

## 10. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서 S3 권한을 어떻게 관리할 것인가?
- 애플리케이션 Pod에는 필요한 S3 Prefix에 대한 최소 권한만 제공한다.
- S3_BUCKET, S3_PREFIX 같은 일반 설정은 ConfigMap으로 관리할 수 있다.
- AWS Access Key, Secret Access Key 같은 민감 정보는 Secret으로 관리해야 한다.
- Pod가 raw, clean, feature, log, artifact 전체를 무제한으로 삭제할 수 있게 하면 안 된다.
- OpenShift에서 실행되는 앱은 주로 필요한 Prefix에 읽기 또는 쓰기 권한만 갖도록 설계한다.

## 11. g4dn 연결

- g4dn GPU 실습에서는 어떤 S3 권한이 필요한가?
- GPU 실습 서버는 학습 데이터 읽기 권한이 필요하다.
- 모델 파일, 추론 결과, 실행 로그를 저장할 Prefix에 쓰기 권한이 필요하다.
- raw 원본 삭제 권한은 필요하지 않다.
- 모델 산출물 저장 위치는 users/student/artifact/week7/ 또는 users/student/log/week7/처럼 분리하는 것이 좋다.
- GPU 실습 결과는 용량이 커질 수 있으므로 Lifecycle 기준과 삭제 승인 기준을 함께 정해야 한다.

## 12. 사고 예방 시나리오

| 사고 | 예방 방법 |
|---|---|
| raw 삭제 | raw Prefix에는 DeleteObject 권한을 기본적으로 부여하지 않는다. |
| 다른 개인 Prefix 업로드 | users/student/ Prefix로 접근 범위를 제한한다. |
| log 삭제 | log Prefix에는 삭제 권한을 제한하고, 조회와 업로드 중심으로 허용한다. |
| artifact 삭제 | 최종 산출물 Prefix는 삭제 전 승인 절차를 둔다. |
| Lifecycle 오설정 | PutLifecycleConfiguration 권한은 강사/관리자에게만 허용한다. |
| Access Key 노출 | .env를 Git에 올리지 않고, Secret과 환경 변수 관리를 분리한다. |

## 13. 생성한 산출물

| 산출물 | 경로 |
|---|---|
| IAM 운영 규칙 Markdown | outputs/day4_s3_iam_operation_rules.md |
| IAM 운영 규칙 JSON | outputs/day4_s3_iam_operation_rules.json |
| 개인 권한 매트릭스 | outputs/day4_s3_personal_permission_matrix.md |

## 14. 오늘 이해한 점

-

## 15. 다음 교시에서 할 일

Day 4 산출물 정리 + Day 5 예고
