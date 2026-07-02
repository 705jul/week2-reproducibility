# 2주차 Day 5 1교시 실습 기록지

## 작성자

- author: kim-juil

## 1. 오늘 주제

S3 데이터 로딩 → 전처리 재사용 → 베이스라인 준비

## 2. Day 1~4 연결

| Day | 내가 만든 것 | Day 5에서 어떻게 쓰는가 |
|---|---|---|
| Day 1 | 데이터 관찰 결과 | 데이터 검증 기준 |
| Day 2 | clean 데이터 | S3에서 다시 읽을 입력 데이터 |
| Day 3 | 재현성 구조 | seed, requirements, .env, src 재사용 |
| Day 4 | S3 운영 구조 | clean 입력, feature/log/artifact 출력 Prefix |

## 3. Day 5 통합 파이프라인

```text
S3 clean 데이터
↓
Notebook
↓
데이터 검증
↓
feature 생성
↓
train / validation / test split
↓
baseline model 준비
↓
metrics / report / run_info 저장
↓
S3 업로드
```

## 4. baseline 의미

- baseline model이란?
  - 복잡한 모델을 만들기 전에 기준점으로 사용하는 가장 기본적인 모델이다.
  - 이후 모델 성능이 좋아졌는지 비교하기 위한 기준 성능을 만든다.

- Day 5에서 최고 성능을 목표로 하지 않는 이유는?
  - Day 5의 핵심은 모델 성능 경쟁이 아니라 재현 가능한 데이터 파이프라인을 만드는 것이다.
  - S3에서 clean 데이터를 읽고, feature를 만들고, split하고, 기록을 남기는 구조가 먼저 필요하다.

## 5. leakage 주의

| 위험 상황 | 왜 위험한가 |
|---|---|
| 전체 데이터로 평균 계산 후 split | test 데이터 정보가 train 과정에 섞일 수 있다. |
| test 데이터 보고 전처리 기준 결정 | 최종 평가용 데이터를 미리 본 것이 되어 성능이 과대평가될 수 있다. |
| churn과 같은 의미의 컬럼 사용 | target 정답을 간접적으로 알려주는 컬럼이 들어갈 수 있다. |
| test 성능 보고 feature 반복 수정 | test 데이터가 검증용처럼 사용되어 최종 평가 의미가 약해진다. |

## 6. 개인 S3 설정

| 항목 | 값 |
|---|---|
| author | kim-juil |
| bucket | edu-ai-lake |
| clean S3 URI | s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv |
| feature Prefix | users/kim-juil/feature/customers/ |
| log Prefix | users/kim-juil/log/week2/ |
| artifact Prefix | users/kim-juil/artifact/week2/ |

## 7. OpenShift Local 연결

- 같은 프로젝트 구조를 OpenShift Local에서도 실행하려면 무엇이 같아야 하는가?
- 같은 `requirements.txt`를 사용해야 한다.
- 같은 `.env.example` 구조를 유지해야 한다.
- 같은 `src` 모듈 구조를 사용해야 한다.
- 같은 S3 Bucket과 Prefix 설정을 환경 변수 또는 ConfigMap으로 주입할 수 있어야 한다.
- AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 관리해야 한다.

## 8. g4dn 연결

- Day 5에서 g4dn을 사용하지 않는 이유는?
  - Day 5는 데이터 로딩, feature 생성, split, baseline 준비가 중심이므로 GPU가 필요하지 않다.

- 이후 GPU 실습에서 Day 5 구조가 어떻게 쓰이는가?
  - Day 5에서 만든 feature, log, artifact 저장 규칙을 그대로 사용할 수 있다.
  - 이후 g4dn에서 생성한 모델 파일, 추론 결과, 실행 로그를 S3 artifact/log Prefix에 저장할 수 있다.

## 9. 오늘 생성한 산출물

| 산출물 | 경로 |
|---|---|
| Day 5 Notebook | notebooks/05_s3_to_baseline_pipeline.ipynb |
| 오리엔테이션 JSON | outputs/day5_orientation_record.json |
| 오리엔테이션 Markdown | outputs/day5_orientation_record.md |
| 1교시 개인 실습 기록지 | reports/week2/day5_period1_orientation_record.md |

## 10. 오늘 이해한 점

-

## 11. 다음 교시에서 할 일

S3에서 clean 데이터를 가져오기 + 로컬/OpenShift Local 경로 정리
