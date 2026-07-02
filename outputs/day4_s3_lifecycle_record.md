# Day 4 6교시 S3 Lifecycle 실습 기록
## 1. 작성자
- author: student
## 2. 버킷
- bucket: edu-ai-lake
## 3. 오늘 주제
S3 Lifecycle 개념 + 보관 정책 설계
## 4. 오늘 이해한 핵심
Lifecycle은 오래된 객체를 저비용 스토리지로 전환하거나
일정 기간 후 만료 처리하는 S3 보관 정책이다.
Versioning은 복구 가능성을 높이고,
Lifecycle은 오래된 객체와 이전 버전의 보관 비용을 관리한다.
## 5. Transition
Transition은 객체를 다른 스토리지 클래스로 전환하는 것이다.
예:
- 오래된 log 전환
- 오래된 artifact 전환
- archive 데이터 장기 보관 전환
## 6. Expiration
Expiration은 일정 기간 후 객체를 만료 처리하는 것이다.
자동 삭제와 연결되므로 매우 조심해야 한다.
## 7. Prefix별 보관 설계 요약
| Prefix | 보관 기준 | 만료 기준 |
|---|---|---|
| raw | 장기 보관 | 자동 만료 금지 |
| clean | 중기/장기 보관 | 재생성 가능성 확인 후 검토 |
| feature | 단기/중기 보관 | 모델 연결 확인 후 검토 |
| notebook | 과정 기간 보관 | 교육 기준에 따름 |
| artifact | 평가 기간 보관 | 최종 산출물 자동 삭제 제한 |
| log | 추적 기간 보관 | 자동 삭제 신중 |
| archive | 장기 보관 | 승인 전 삭제 금지 |
| tmp | 짧게 보관 | 7~30일 만료 후보 |
| versioning-test | 짧게 보관 | 14~30일 만료 후보 |
## 8. raw 삭제 제한 이유
raw는 원본 재현 기준이다.
raw가 삭제되면 clean, feature, model 실험을 다시 재현하기 어려워진다.
따라서 raw는 자동 삭제 정책 대상에서 제외하거나, 삭제 전 승인을 요구해야 한다.
## 9. Versioning과 Lifecycle 연결
Versioning이 켜지면 이전 버전이 계속 쌓일 수 있다.
이전 버전도 저장 비용을 발생시킨다.
따라서 오래된 이전 버전 관리 정책이 필요하다.
단, raw와 최종 산출물의 이전 버전은 삭제 전 승인이 필요하다.
## 10. 생성한 산출물
| 산출물 | 경로 |
|---|---|
| Lifecycle 설계 Markdown | outputs/day4_s3_lifecycle_design.md |
| Lifecycle 설계 JSON | outputs/day4_s3_lifecycle_design.json |
| 실습용 tmp 정책 예시 JSON | outputs/day4_s3_lifecycle_tmp_policy_example.json |
| Lifecycle 기록 Markdown | outputs/day4_s3_lifecycle_record.md |
## 11. OpenShift 연결
OpenShift Local 또는 Developer Sandbox에서 생성한 log, artifact, feature도 같은 S3 Lifecycle 기준을 따른다.
## 12. g4dn 연결
GPU 실습 주차에서 생성한 모델 파일, GPU 결과, 실행 로그도 Lifecycle 정책 설계 대상이 된다.
## 13. 다음 교시 연결
7교시에서는 이 보관 정책을 누가 적용하고,
누가 삭제할 수 있으며,
누가 raw와 artifact를 보호해야 하는지 IAM 최소 권한과 개인 운영 규칙으로 연결한다.
