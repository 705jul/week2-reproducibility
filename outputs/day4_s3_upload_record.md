# Day 4 3교시 S3 업로드 기록

## 1. 작성자

- author: student

## 2. 버킷

- bucket: edu-ai-lake

## 3. 업로드 목적

Day 1~3에서 만든 raw 데이터, clean 데이터, 실행 기록, 리포트 산출물을  
S3 Prefix 구조에 맞게 업로드했다.

핵심은 파일을 올리는 것이 아니라  
데이터 상태에 맞는 위치에 올리는 것이다.

## 4. 업로드한 파일

| 구분 | 로컬 파일 | S3 위치 | 원칙 |
|---|---|---|---|
| raw | data/raw/customers_raw.csv | s3://edu-ai-lake/users/student/raw/customers/customers_raw_20260605_v1.csv | 원본, 덮어쓰기 금지 |
| clean | data/clean/customers_clean_20260606_v2.csv | s3://edu-ai-lake/users/student/clean/customers/customers_clean_20260606_v2.csv | 전처리 완료, 날짜/버전 포함 |
| log | outputs/run_info.json | s3://edu-ai-lake/users/student/log/week2/run_info_20260606_student.json | 실행 조건 기록 |
| artifact | reports/week2/day3_reproducibility_final_report.md | s3://edu-ai-lake/users/student/artifact/week2/day3_reproducibility_final_report_student.md | 리포트 산출물 |

## 5. 업로드 확인 명령

```bash
aws s3 ls s3://edu-ai-lake/users/student/ --recursive
```

## 6. raw 데이터 원칙

- raw 데이터는 원본이다.
- raw 데이터는 수정하지 않는다.
- raw 데이터는 같은 이름으로 무심코 덮어쓰지 않는다.
- raw 데이터는 쉽게 삭제하지 않는다.
- 변경이 필요하면 새 파일명과 새 버전으로 업로드한다.

## 7. clean 데이터 원칙

- clean 데이터는 전처리 완료 데이터이다.
- raw와 같은 위치에 섞지 않는다.
- 파일명에 날짜와 버전을 포함한다.
- 처리 기준은 log 또는 artifact와 함께 보관한다.

## 8. log / artifact 원칙

- run_info.json은 log/에 저장한다.
- 리포트와 제출 산출물은 artifact/에 저장한다.
- log는 실행 조건 추적용이다.
- artifact는 결과 산출물 보관용이다.

## 9. OpenShift / g4dn 연결

- OpenShift Local 또는 Developer Sandbox에서도 같은 S3 Prefix를 사용할 수 있다.
- g4dn.xlarge는 이번 교시에서 사용하지 않는다.
- 이후 GPU 실습 결과는 users/student/artifact/week7/ 또는 users/student/log/week7/에 저장할 수 있다.

## 10. 다음 교시 연결

4교시에서는 final.csv, new.csv 같은 애매한 파일명을 피하고,  
dataset_stage_yyyymmdd_version 형식의 파일명 규칙과 데이터 적재 규칙을 문서화한다.
