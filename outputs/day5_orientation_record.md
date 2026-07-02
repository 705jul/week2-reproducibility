# Day 5 오리엔테이션 기록

## 1. 작성자

- author: kim-juil

## 2. Day 5 주제

S3 데이터 로딩 → 전처리 재사용 → feature 생성 → split → baseline 준비

## 3. Day 5 목표

- S3에서 clean 데이터를 가져온다.
- 데이터 구조를 검증한다.
- feature 데이터를 생성한다.
- train / validation / test로 분리한다.
- baseline model을 준비한다.
- metrics와 report를 저장한다.
- 결과물을 S3에 다시 업로드한다.
- 3주차 모델링 수업으로 연결한다.

## 4. 통합 파이프라인 구조

```text
S3 clean 데이터
↓
개인 로컬 PC WSL2 / Notebook
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
S3 feature / log / artifact 업로드
```

## 5. Day 5 입력 데이터

```text
s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv
```

## 6. S3 출력 Prefix

| 구분 | Prefix |
|---|---|
| feature | users/kim-juil/feature/customers/ |
| log | users/kim-juil/log/week2/ |
| artifact | users/kim-juil/artifact/week2/ |

## 7. 주의사항

- Day 5의 목표는 최고 성능 모델이 아니다.
- baseline은 기준 성능 확인용이다.
- test 데이터는 최종 평가용으로 아껴야 한다.
- leakage를 항상 점검해야 한다.
- 실행 기록과 산출물을 남겨야 한다.
- 개인 author와 개인 Prefix를 사용한다.
- Day 5에서는 g4dn.xlarge를 사용하지 않는다.
- OpenShift Local에서도 같은 프로젝트 구조와 S3 경로를 사용할 수 있어야 한다.

## 8. OpenShift Local 연결

Day 5 기본 실행은 개인 로컬 PC WSL2에서 진행한다.

다만 같은 프로젝트 구조, 같은 requirements.txt, 같은 .env.example, 같은 src 모듈을 유지해서  
OpenShift Local 환경에서도 동일한 파이프라인을 실행할 수 있도록 준비한다.

OpenShift에서는 S3 경로 정보를 ConfigMap 또는 환경 변수로 주입할 수 있다.

예시:

```text
S3_BUCKET=edu-ai-lake
S3_CLEAN_KEY=users/kim-juil/clean/customers/customers_clean_20260606_v2.csv
S3_FEATURE_PREFIX=users/kim-juil/feature/customers/
S3_LOG_PREFIX=users/kim-juil/log/week2/
S3_ARTIFACT_PREFIX=users/kim-juil/artifact/week2/
```

AWS 인증 정보는 Secret 또는 더 안전한 인증 방식으로 관리한다.

## 9. g4dn.xlarge 연결

Day 5에서는 GPU가 필요하지 않으므로 g4dn.xlarge를 사용하지 않는다.

이후 GPU 실습 주차에서는 Day 5에서 만든 feature, log, artifact 저장 규칙을 그대로 사용한다.

예를 들어 g4dn에서 생성한 모델 파일, 추론 결과, 실행 로그는 다음 Prefix 체계로 저장할 수 있다.

```text
users/kim-juil/artifact/week7/
users/kim-juil/log/week7/
```

## 10. 핵심 메시지

최고 성능 모델을 만드는 것이 아니라,  
모델링으로 넘어갈 수 있는 재현 가능한 데이터 파이프라인을 만드는 것이 목표다.
