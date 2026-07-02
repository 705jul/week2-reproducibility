# 2주차 Day 4 2교시 실습 기록지

## 작성자

## 1. 오늘 주제

S3 버킷 / Prefix 구조 설계

## 2. 버킷 개념

- S3 버킷이란?

## 3. Prefix 개념

- Prefix란?

## 4. 버킷 이름

- bucket:

## 5. 개인 author

- author:

## 6. 기본 전략

- 선택 전략:
- 선택 이유:

## 7. 공통 Prefix

| Prefix | 목적 |
|---|---|
| common/raw/customers/ |  |
| common/reference/week2/ |  |

## 8. 개인 Prefix

| Prefix | 목적 |
|---|---|
| users/&lt;author&gt;/raw/customers/ |  |
| users/&lt;author&gt;/clean/customers/ |  |
| users/&lt;author&gt;/feature/customers/ |  |
| users/&lt;author&gt;/notebook/week2/ |  |
| users/&lt;author&gt;/artifact/week2/ |  |
| users/&lt;author&gt;/log/week2/ |  |
| users/&lt;author&gt;/archive/ |  |

## 9. 3교시 업로드 계획

| 로컬 파일 | S3 Prefix |
|---|---|
| data/raw/customers_raw.csv |  |
| data/clean/customers_clean_20260606_v2.csv |  |
| outputs/run_info.json |  |

## 10. OpenShift 연결

- OpenShift Local 또는 Developer Sandbox에서 같은 Prefix를 어떻게 사용할 것인가?

## 11. g4dn 연결

- g4dn GPU 실습 결과는 어느 Prefix에 저장할 것인가?

## 12. 오늘 이해한 점

-
