# 2주차 Day 4 6교시 실습 기록지

## 작성자

- author: student

## 1. 오늘 주제

S3 Lifecycle 개념 + 보관 정책 설계

## 2. Lifecycle 개념

- Lifecycle이란?
- S3 객체의 보관 기간, 스토리지 클래스 전환, 만료, 이전 버전 정리, 미완료 멀티파트 업로드 정리 등을 자동화하는 수명 주기 관리 기능이다.

## 3. Transition

- 의미:
  - 객체를 일정 기간이 지난 뒤 더 저렴한 스토리지 클래스로 이동하는 작업이다.
- 적용 후보 Prefix:
  - users/student/clean/customers/
  - users/student/feature/customers/
  - users/student/log/week2/
  - users/student/artifact/week2/
- 주의할 점:
  - 자주 조회하는 데이터는 너무 빨리 전환하지 않는다.
  - raw 데이터는 원본성이 중요하므로 전환 전 보관 기준을 명확히 정한다.
  - 복원이 필요한 스토리지 클래스로 전환하면 조회 지연이나 복원 비용이 발생할 수 있다.

## 4. Expiration

- 의미:
  - 객체를 일정 기간이 지난 뒤 만료 처리하거나 삭제 대상으로 만드는 작업이다.
- 적용 후보 Prefix:
  - users/student/tmp/
  - users/student/clean/customers/versioning-test/
- 주의할 점:
  - raw, log, 최종 artifact에는 위험한 자동 삭제를 바로 적용하지 않는다.
  - 실습용 tmp Prefix처럼 재생성 가능하고 중요도가 낮은 데이터에 먼저 적용한다.
  - 정책 적용 전 Prefix 범위를 반드시 확인한다.

## 5. Versioning과 Lifecycle 관계

- Versioning이 왜 비용과 연결되는가?
  - 같은 Key에 여러 번 업로드하면 이전 버전이 계속 남을 수 있고, 남아 있는 모든 버전이 저장 비용에 포함될 수 있기 때문이다.
- Noncurrent version은 무엇인가?
  - 현재 최신 버전이 아닌 이전 객체 버전을 의미한다.
- 오래된 이전 버전은 어떻게 관리해야 하는가?
  - 중요 데이터는 충분한 보관 기간을 둔다.
  - 실습용 또는 테스트용 이전 버전은 일정 기간 후 정리하는 Lifecycle 규칙을 검토한다.
  - 삭제 전 VersionId, Prefix, 보관 필요 여부를 확인한다.

## 6. raw 보관 정책

| 항목 | 내용 |
|---|---|
| Prefix | users/student/raw/customers/ |
| 보관 기준 | 원본 데이터이므로 장기 보관 |
| 자동 삭제 여부 | 기본적으로 자동 삭제하지 않음 |
| 삭제 전 승인 필요 여부 | 필요 |
| 이유 | raw 데이터는 원본이므로 재현성과 감사 추적의 기준이 된다. |

## 7. clean 보관 정책

| 항목 | 내용 |
|---|---|
| Prefix | users/student/clean/customers/ |
| 보관 기준 | 전처리 기준과 버전이 명확한 데이터는 보관 |
| 전환 기준 | 장기간 조회하지 않는 clean 데이터는 저비용 스토리지 전환 검토 |
| 만료 기준 | 운영 기준 없이 자동 만료 금지 |
| 이유 | clean 데이터는 모델 학습과 분석의 기준 데이터로 다시 사용될 수 있다. |

## 8. feature 보관 정책

| 항목 | 내용 |
|---|---|
| Prefix | users/student/feature/customers/ |
| 보관 기준 | 모델 학습에 사용한 feature 데이터는 모델 버전과 함께 보관 |
| 재생성 가능 여부 | clean 데이터와 feature 생성 코드가 있으면 재생성 가능 |
| 모델 연결 확인 여부 | 필요 |
| 이유 | 모델 성능 재현과 데이터 누수 검증에 필요하다. |

## 9. log 보관 정책

| 항목 | 내용 |
|---|---|
| Prefix | users/student/log/week2/ |
| 보관 기준 | 실행 조건, 입력 파일, 출력 파일, seed, author 추적용으로 보관 |
| 전환 기준 | 오래된 로그는 저비용 스토리지 전환 검토 |
| 자동 삭제 주의 여부 | 매우 주의 필요 |
| 이유 | 장애 분석, 실험 재현, 업로드 추적에 필요하다. |

## 10. artifact 보관 정책

| 항목 | 내용 |
|---|---|
| Prefix | users/student/artifact/week2/ |
| 보관 기준 | 리포트, 제출물, 모델 파일, 결과 산출물 보관 |
| 최종 산출물 삭제 제한 여부 | 제한 필요 |
| 이유 | 교육 제출물과 실험 결과의 증빙 자료이기 때문이다. |

## 11. tmp / versioning-test 정책

| Prefix | 보관 기준 | 만료 후보 기간 |
|---|---|---|
| users/student/tmp/ | 실습용 임시 파일만 저장 | 7일 |
| users/student/clean/customers/versioning-test/ | Versioning 실습용 테스트 객체만 저장 | 이전 버전 30일 |

## 12. 생성한 산출물

| 산출물 | 경로 |
|---|---|
| Lifecycle 설계 Markdown | outputs/day4_s3_lifecycle_design.md |
| Lifecycle 설계 JSON | outputs/day4_s3_lifecycle_design.json |
| 실습용 tmp 정책 예시 JSON | outputs/day4_s3_lifecycle_tmp_policy_example.json |
| Lifecycle 기록 Markdown | outputs/day4_s3_lifecycle_record.md |

## 13. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서 Lifecycle 기준이 필요한 이유는?
- OpenShift에서 실행되는 Pod가 S3에 로그, 결과 파일, 중간 산출물을 계속 저장할 수 있기 때문이다.
- Prefix별 보관 정책이 없으면 임시 파일과 중요한 산출물이 섞여 관리가 어려워진다.
- tmp, log, artifact의 보관 기준을 분리하면 운영 실수와 비용 증가를 줄일 수 있다.

## 14. g4dn 연결

- g4dn GPU 실습 결과에 Lifecycle이 필요한 이유는?
- GPU 실습 결과는 모델 파일, 추론 결과, 로그, 성능 측정 결과처럼 용량이 커질 수 있는 산출물을 만들 수 있다.
- 비용이 큰 산출물은 보관 기준, 전환 기준, 삭제 승인 기준을 미리 정해야 한다.
- 최종 모델과 제출 산출물은 artifact로 보관하고, 임시 테스트 결과는 tmp 또는 log 기준으로 관리한다.

## 15. 오늘 이해한 점

-

## 16. 다음 교시에서 할 일

IAM 최소 권한 + 개인 운영 규칙
