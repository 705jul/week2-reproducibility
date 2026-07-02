# Day 4 개인 S3 권한 매트릭스
## 1. 작성자
- author: student
## 2. 버킷
- bucket: edu-ai-lake
## 3. 개인 Prefix
- users/student/
## 4. Prefix별 권한 매트릭스
| Prefix | List | Get | Put | Delete | 비고 |
|---|---|---|---|---|---|
| users/student/raw/customers/ | 허용 | 허용 | 제한 | 금지 | 원본 보호 |
| users/student/clean/customers/ | 허용 | 허용 | 허용 | 제한 | Day 5 입력 |
| users/student/feature/customers/ | 허용 | 허용 | 허용 | 제한 | 모델 연결 확인 |
| users/student/notebook/week2/ | 허용 | 허용 | 허용 | 제한 | 실습 기록 |
| users/student/artifact/week2/ | 허용 | 허용 | 허용 | 제한 | 평가 산출물 |
| users/student/log/week2/ | 허용 | 허용 | 허용 | 금지 | 실행 추적 |
| users/student/archive/ | 허용 | 허용 | 제한 | 승인 필요 | 장기 보관 |
| users/student/tmp/ | 허용 | 허용 | 허용 | 허용 | 임시 파일 |
## 5. 학생 개인에게 허용하지 않는 작업
- raw DeleteObject
- log DeleteObject
- artifact 최종 산출물 DeleteObject
- DeleteObjectVersion
- PutBucketVersioning
- PutLifecycleConfiguration
- PutBucketPolicy
- DeleteBucket
- 다른 개인 Prefix PutObject
- 다른 개인 Prefix DeleteObject
## 6. 권한 설계 이유
raw는 원본 재현 기준이므로 삭제를 제한한다.
log는 실행 추적 근거이므로 삭제를 제한한다.
artifact는 평가와 제출 근거가 될 수 있으므로 삭제를 제한한다.
tmp는 임시 파일이므로 본인 Prefix 안에서는 삭제를 허용할 수 있다.
## 7. Day 5 연결
Day 5에서는 S3 clean 데이터를 다시 읽어 baseline 준비로 연결한다.
따라서 clean Prefix에 대한 GetObject 권한이 필요하다.
