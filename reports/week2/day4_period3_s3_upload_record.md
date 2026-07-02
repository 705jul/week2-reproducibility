# 2주차 Day 4 3교시 실습 기록지

## 작성자

- author: student

## 1. 오늘 주제

raw / clean 데이터 업로드 실습

## 2. 사용한 버킷

- bucket: edu-ai-lake

## 3. 사용한 author

- author: student

## 4. 사용한 Prefix

| 구분 | Prefix |
|---|---|
| raw | users/student/raw/customers/ |
| clean | users/student/clean/customers/ |
| log | users/student/log/week2/ |
| artifact | users/student/artifact/week2/ |

## 5. 업로드한 파일

| 구분 | 로컬 파일 | 업로드 여부 |
|---|---|---|
| raw | data/raw/customers_raw.csv | 확인 필요 |
| clean | data/clean/customers_clean_20260606_v2.csv | 확인 필요 |
| log | outputs/run_info.json | 확인 필요 |
| artifact | reports/week2/day3_reproducibility_final_report.md | 확인 필요 |

## 6. S3 업로드 경로

| 구분 | S3 URI |
|---|---|
| raw | s3://edu-ai-lake/users/student/raw/customers/customers_raw_20260605_v1.csv |
| clean | s3://edu-ai-lake/users/student/clean/customers/customers_clean_20260606_v2.csv |
| log | s3://edu-ai-lake/users/student/log/week2/run_info_20260606_student.json |
| artifact | s3://edu-ai-lake/users/student/artifact/week2/day3_reproducibility_final_report_student.md |

## 7. 업로드 확인 명령

```bash
aws s3 ls s3://edu-ai-lake/users/student/ --recursive
```

## 8. 업로드 결과

| 항목 | 결과 |
|---|---|
| raw 객체 확인 |  |
| clean 객체 확인 |  |
| log 객체 확인 |  |
| artifact 객체 확인 |  |

## 9. raw 데이터 원칙

- raw 데이터는 왜 덮어쓰면 안 되는가?

## 10. clean 데이터 원칙

- clean 데이터 파일명에는 왜 날짜와 버전이 들어가야 하는가?

## 11. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서 같은 S3 Prefix를 어떻게 사용할 것인가?

## 12. g4dn 연결

- g4dn GPU 실습 결과는 어느 Prefix에 저장할 것인가?

## 13. 오늘 이해한 점

-

## 14. 다음 교시에서 할 일

파일명 규칙 + 데이터 적재 규칙 문서화
