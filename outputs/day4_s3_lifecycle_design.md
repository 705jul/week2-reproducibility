# Day 4 S3 Lifecycle 보관 정책 설계
## 1. 작성자
- author: student
## 2. 버킷
- bucket: edu-ai-lake
## 3. 주제
S3 Lifecycle 개념 + 보관 정책 설계
## 4. 핵심 개념
S3 Lifecycle은 객체를 일정 조건에 따라 다른 스토리지 클래스로 전환하거나,
일정 기간 후 만료 처리하는 규칙이다.
Lifecycle은 삭제 도구가 아니라 보관 정책이다.
Versioning은 복구 가능성을 높이고,
Lifecycle은 오래된 객체와 이전 버전의 보관 비용을 관리한다.
## 5. Transition
Transition은 객체를 다른 스토리지 클래스로 전환하는 것이다.
예:
- 오래된 log를 저비용 스토리지로 전환
- 오래된 artifact를 장기 보관 스토리지로 전환
- archive 데이터를 장기 보관 스토리지로 전환 검토
## 6. Expiration
Expiration은 일정 기간 후 객체를 만료 처리하는 것이다.
자동 삭제에 가까운 동작이므로 매우 조심해야 한다.
raw, 최종 artifact, 주요 log에는 자동 만료 정책을 신중하게 적용해야 한다.
## 7. Prefix별 보관 정책
| Prefix | 의미 | 보관 기준 | 전환 기준 | 만료 기준 | 주의 |
|---|---|---|---|---|---|
| users/student/raw/customers/ | 원본 데이터 | 장기 보관 | 장기 보관 전환 검토 | 자동 만료 금지 | 삭제 전 승인 |
| users/student/clean/customers/ | 전처리 완료 데이터 | 중기/장기 | 일정 기간 후 전환 검토 | 재생성 가능성 확인 후 검토 | Day 5 입력 |
| users/student/feature/customers/ | 모델 학습용 데이터 | 단기/중기 | 모델 연결 종료 후 전환 검토 | 재생성 가능 시 검토 | 모델 버전 확인 |
| users/student/notebook/week2/ | 실습 Notebook | 과정 기간 보관 | 과정 종료 후 전환 검토 | 교육 기준에 따름 | 실행 과정 근거 |
| users/student/artifact/week2/ | 리포트/산출물 | 평가 기간 보관 | 평가 후 전환 검토 | 최종 산출물 자동 삭제 제한 | 평가 근거 |
| users/student/log/week2/ | 실행 기록 | 추적 기간 보관 | 일정 기간 후 archive 검토 | 자동 삭제 신중 | 원인 분석 근거 |
| users/student/archive/ | 장기 보관 | 장기 보관 | 장기 보관 스토리지 검토 | 승인 전 삭제 금지 | 휴지통 아님 |
| users/student/tmp/ | 임시 파일 | 짧게 보관 | 보통 불필요 | 7~30일 만료 후보 | 실제 적용 후보 |
| users/student/clean/customers/versioning-test/ | Versioning 실습 파일 | 짧게 보관 | 보통 불필요 | 14~30일 만료 후보 | 실습 객체 |
## 8. raw 보관 원칙
- raw는 원본이다.
- raw는 모든 clean, feature, model 실험의 재현 기준이다.
- raw는 자동 삭제하지 않는다.
- raw 삭제는 개인이 임의로 하지 않는다.
- raw 삭제 전에는 강사 또는 관리자 승인이 필요하다.
## 9. clean 보관 원칙
- clean은 분석과 모델링 입력 후보이다.
- Day 5에서 clean 데이터를 다시 읽어 baseline 준비로 연결한다.
- clean 삭제 전에는 raw, 전처리 코드, run_info가 남아 있는지 확인한다.
- 일정 기간 후 저비용 스토리지 전환을 검토할 수 있다.
## 10. feature 보관 원칙
- feature는 모델 학습용 데이터이다.
- 재생성 가능하면 단기/중기 보관 후 정리할 수 있다.
- 특정 모델 버전과 연결되어 있다면 삭제 전 모델 기록을 확인해야 한다.
- split 기준과 누수 점검 기록이 필요하다.
## 11. log 보관 원칙
- log는 실행 조건 추적용이다.
- run_info, upload record, versioning record, lifecycle design record를 보관한다.
- 결과가 달라졌을 때 원인 분석에 필요하다.
- 자동 삭제는 신중하게 검토한다.
## 12. artifact 보관 원칙
- artifact는 리포트, 제출물, 모델 파일 같은 결과 산출물이다.
- 최종 제출 산출물은 자동 삭제하지 않는다.
- 평가 기간 이후 전환을 검토할 수 있다.
## 13. tmp / versioning-test 정책
- tmp는 임시 파일이므로 짧은 기간 후 만료 후보이다.
- versioning-test는 실습용 객체이므로 장기 보관할 필요가 낮다.
- 실제 Lifecycle 적용 실습은 raw가 아니라 tmp 또는 versioning-test에만 진행한다.
## 14. Versioning과 Lifecycle 연결
- Versioning은 이전 버전을 보존한다.
- 이전 버전도 저장 공간을 사용한다.
- 오래된 이전 버전은 일정 기간 후 전환 또는 만료 검토가 필요하다.
- 단, raw와 최종 산출물의 이전 버전은 삭제 전 승인 기준이 필요하다.
## 15. OpenShift 연결
- OpenShift Local 또는 Developer Sandbox에서 생성한 파일도 같은 S3 Prefix와 Lifecycle 기준을 따른다.
- OpenShift Job이나 Workbench에서 생성한 log는 log/ Prefix에 저장한다.
- S3_BUCKET, S3_LOG_PREFIX, S3_ARTIFACT_PREFIX는 환경 변수 또는 ConfigMap으로 주입할 수 있다.
- AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 관리한다.
## 16. g4dn 연결
- Day 4에서는 g4dn.xlarge를 사용하지 않는다.
- GPU 실습 주차에서 생성되는 모델 파일, CUDA 결과, GPU 실행 로그도 Lifecycle 대상이 될 수 있다.
- 모델 파일은 artifact/week7/ 또는 model/ 확장 Prefix에서 장기 보관을 검토한다.
- GPU 임시 결과는 tmp/ 또는 log/week7/ 기준으로 보관 기간을 정한다.
## 17. 다음 교시 연결
7교시에서는 이 보관 정책을 누가 적용하고,
누가 삭제할 수 있으며,
누가 raw를 보호해야 하는지 IAM 최소 권한과 개인 운영 규칙으로 연결한다.
