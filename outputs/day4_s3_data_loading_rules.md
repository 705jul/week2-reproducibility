# Day 4 S3 데이터 적재 규칙

## 1. 작성자

- author: kim-juil

## 2. 버킷

- bucket: edu-ai-lake

## 3. Prefix 구조

| Prefix | 역할 |
|---|---|
| users/kim-juil/raw/customers/ | 원본 고객 데이터 |
| users/kim-juil/clean/customers/ | 전처리 완료 고객 데이터 |
| users/kim-juil/feature/customers/ | 모델 학습용 고객 feature 데이터 |
| users/kim-juil/notebook/week2/ | Week 2 Notebook |
| users/kim-juil/artifact/week2/ | Week 2 리포트와 산출물 |
| users/kim-juil/log/week2/ | Week 2 실행 기록과 업로드 기록 |
| users/kim-juil/archive/ | 장기 보관 데이터 |

## 4. 파일명 규칙

형식:

```text
{dataset}_{stage}_{yyyymmdd}_v{version}.{ext}
```

예:

```text
customers_clean_20260606_v2.csv
```

## 5. raw 데이터 규칙

- 원본 데이터만 저장한다.
- 수정하지 않는다.
- 덮어쓰지 않는다.
- 쉽게 삭제하지 않는다.
- 변경이 필요하면 새 파일명과 새 버전으로 업로드한다.
- 원본 출처와 업로드 시각을 기록한다.

## 6. clean 데이터 규칙

- 전처리 완료 데이터를 저장한다.
- 처리 기준은 리포트 또는 run_info에 기록한다.
- 파일명에 날짜와 버전을 포함한다.
- raw 데이터와 같은 위치에 섞지 않는다.
- 어떤 raw 데이터에서 만들어졌는지 기록한다.

## 7. feature 데이터 규칙

- 모델 학습용 특징 데이터를 저장한다.
- train/test split 기준을 기록한다.
- 데이터 누수 위험 여부를 점검한다.
- 어떤 clean 데이터에서 만들어졌는지 기록한다.
- 재생성 가능 여부를 기록한다.
- 가능하면 Parquet 형식을 우선 검토한다.

## 8. log 데이터 규칙

- run_info.json을 저장한다.
- 업로드 기록 JSON과 Markdown을 저장한다.
- 실행 날짜, 입력 파일, 출력 파일, seed, author를 기록한다.
- 실험 결과가 달라졌을 때 원인 추적에 사용한다.
- 임의 삭제하지 않는다.

## 9. artifact 데이터 규칙

- 리포트, 결과 산출물, 모델 파일을 저장한다.
- 최종 제출 산출물은 쉽게 삭제하지 않는다.
- 파일명에 날짜와 author를 포함한다.
- log와 artifact의 역할을 구분한다.
- log는 실행 조건 기록이고 artifact는 결과 산출물이다.

## 10. notebook 데이터 규칙

- 실습 Notebook을 저장한다.
- 실행 순서와 Markdown 설명을 포함한다.
- 필요 시 출력 결과 포함 여부를 교육 기준에 맞춘다.
- 파일명에 주차, Day, 날짜, 버전을 포함할 수 있다.

## 11. archive 규칙

- 오래되었지만 보존해야 하는 데이터를 저장한다.
- Lifecycle 정책 또는 승인 기준에 따라 이동한다.
- 삭제 전 확인 절차를 거친다.

## 12. 삭제 제한 대상

- raw/
- log/
- 최종 제출 artifact/
- 다른 개인의 users/ Prefix
- 출처 확인이 되지 않은 공통 데이터

## 13. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서도 같은 S3 Prefix를 사용한다.
- S3_BUCKET, S3_CLEAN_PREFIX, S3_LOG_PREFIX는 환경 변수 또는 ConfigMap으로 주입할 수 있다.
- AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 다룬다.

## 14. g4dn 연결

- Day 4에서는 g4dn.xlarge를 사용하지 않는다.
- GPU 실습 주차에서는 g4dn 실행 결과를 users/kim-juil/artifact/week7/ 또는 users/kim-juil/log/week7/에 저장한다.
- GPU 실행 로그에도 파일명 규칙을 적용한다.

## 15. 다음 교시 연결

5교시에서는 같은 파일명으로 다시 업로드했을 때  
S3 Versioning이 어떻게 동작하는지 확인한다.
