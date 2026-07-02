# 2주차 Day 4 4교시 실습 기록지

## 작성자

- author: kim-juil

## 1. 오늘 주제

파일명 규칙 + 데이터 적재 규칙 문서화

## 2. 나쁜 파일명 예시

- customers.csv
- customers_final.csv
- final.csv

## 3. 좋은 파일명 예시

- customers_raw_20260605_v1.csv
- customers_clean_20260606_v2.csv
- customers_feature_20260607_v1.parquet

## 4. 기본 파일명 규칙

- 형식: `{dataset}_{stage}_{yyyymmdd}_v{version}.{ext}`
- dataset 의미: 데이터셋 이름
- stage 의미: 데이터 상태 또는 산출물 유형
- yyyymmdd 의미: 생성일 또는 기준일
- version 의미: 데이터 또는 산출물 버전
- ext 의미: 파일 확장자

## 5. stage별 저장 위치

| stage | 의미 | 저장 Prefix |
|---|---|---|
| raw | 원본 데이터 | users/kim-juil/raw/customers/ |
| clean | 전처리 완료 데이터 | users/kim-juil/clean/customers/ |
| feature | 모델 학습용 특징 데이터 | users/kim-juil/feature/customers/ |
| log | 실행 기록과 업로드 기록 | users/kim-juil/log/week2/ |
| report/artifact | 리포트와 결과 산출물 | users/kim-juil/artifact/week2/ |
| notebook | 실습 Notebook | users/kim-juil/notebook/week2/ |
| archive | 장기 보관 데이터 | users/kim-juil/archive/ |

## 6. raw 데이터 규칙

- raw 데이터는 원본이므로 수정하지 않는다.
- raw 데이터는 같은 이름으로 덮어쓰지 않는다.
- 변경이 필요하면 새 파일명과 새 버전으로 업로드한다.

## 7. clean 데이터 규칙

- clean 데이터는 전처리 완료 데이터를 의미한다.
- raw 데이터와 같은 Prefix에 섞지 않는다.
- 파일명에 날짜와 버전을 포함한다.

## 8. feature 데이터 규칙

- feature 데이터는 모델 학습에 사용할 특징 데이터를 의미한다.
- 어떤 clean 데이터에서 만들어졌는지 기록한다.
- train/test split 기준과 데이터 누수 여부를 함께 확인한다.

## 9. log 데이터 규칙

- 실행 조건, 입력 파일, 출력 파일, seed, author를 기록한다.
- run_info.json, 업로드 기록 JSON, 업로드 기록 Markdown을 저장한다.
- 문제 발생 시 원인 추적에 사용할 수 있도록 임의 삭제하지 않는다.

## 10. artifact 데이터 규칙

- 리포트, 결과 산출물, 모델 파일 등을 저장한다.
- 최종 제출 산출물은 쉽게 삭제하지 않는다.
- log는 실행 조건 기록이고 artifact는 결과 산출물이라는 점을 구분한다.

## 11. 삭제 제한 대상

- raw/
- log/
- 최종 제출 artifact/
- 다른 개인의 users/ Prefix
- 출처 확인이 되지 않은 공통 데이터

## 12. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서도 같은 파일명 규칙을 어떻게 사용할 것인가?

## 13. g4dn 연결

- g4dn GPU 실습 결과에는 어떤 파일명 규칙을 적용할 것인가?

## 14. 생성한 산출물

| 산출물 | 경로 |
|---|---|
| 파일명 규칙 문서 | outputs/day4_s3_file_naming_rules.md |
| 데이터 적재 규칙 문서 | outputs/day4_s3_data_loading_rules.md |
| 데이터 적재 규칙 JSON | outputs/day4_s3_data_loading_rules.json |

## 15. 오늘 이해한 점

-

## 16. 다음 교시에서 할 일

S3 Versioning 개념 + 덮어쓰기 실습
