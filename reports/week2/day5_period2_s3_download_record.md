# 2주차 Day 5 2교시 실습 기록지

## 작성자

- author: kim-juil

## 1. 오늘 주제

S3에서 데이터 가져오기 + 로컬/OpenShift Local 경로 정리

## 2. S3 URI 구조

- bucket: edu-ai-lake
- key: users/kim-juil/clean/customers/customers_clean_20260606_v2.csv
- S3 URI: s3://edu-ai-lake/users/kim-juil/clean/customers/customers_clean_20260606_v2.csv

## 3. 개인 설정

| 항목 | 값 |
|---|---|
| AUTHOR | kim-juil |
| AWS_REGION | ap-northeast-2 |
| S3_BUCKET | edu-ai-lake |
| S3_CLEAN_KEY | users/kim-juil/clean/customers/customers_clean_20260606_v2.csv |
| LOCAL_CLEAN_FILE | /home/soldesk/week2-reproducibility/data/clean/customers_clean_20260606_v2.csv |

## 4. 다운로드 전 확인

| 항목 | 결과 |
|---|---|
| AWS CLI 설치 확인 | 확인 필요 |
| AWS 인증 확인 | 확인 필요 |
| S3 객체 존재 확인 | 확인 필요 |
| 로컬 data/clean 폴더 확인 | 확인 필요 |

## 5. 다운로드 방식

| 방식 | 실행 여부 | 결과 |
|---|---|---|
| AWS CLI `aws s3 cp` | 확인 필요 | 확인 필요 |
| boto3 download_file | 확인 필요 | 확인 필요 |

## 6. pandas 읽기 확인

| 항목 | 값 |
|---|---|
| read_csv 성공 여부 | 확인 필요 |
| row 수 | 확인 필요 |
| column 수 | 확인 필요 |
| 주요 columns | 확인 필요 |

## 7. 생성한 산출물

| 산출물 | 경로 |
|---|---|
| clean 데이터 | data/clean/customers_clean_20260606_v2.csv |
| S3 다운로드 기록 JSON | outputs/s3_download_record.json |
| S3 다운로드 기록 Markdown | outputs/s3_download_record.md |
| S3 유틸 모듈 | src/s3_utils.py |

## 8. OpenShift Local 연결

- OpenShift Local에서 같은 코드를 실행하려면 어떤 설정이 같아야 하는가?
- 같은 프로젝트 폴더 구조를 사용해야 한다.
- 같은 `requirements.txt`를 사용해야 한다.
- 같은 `.env.example` 구조를 유지해야 한다.
- `S3_BUCKET`, `S3_CLEAN_KEY`, `LOCAL_CLEAN_FILE` 같은 설정값을 환경 변수 또는 ConfigMap으로 주입할 수 있어야 한다.
- AWS 인증 정보는 코드에 직접 작성하지 않고 Secret 또는 환경 변수로 관리해야 한다.
- 로컬 절대경로를 하드코딩하지 않고 `Path` 기반 상대경로를 사용해야 한다.

## 9. g4dn 연결

- 이번 교시에서 g4dn을 사용하지 않는 이유는?
  - 이번 교시는 S3 clean 데이터 다운로드와 로컬 경로 정리가 중심이므로 GPU가 필요하지 않다.
  - pandas 기반 CSV 읽기와 데이터 확인은 CPU 환경에서 충분히 수행할 수 있다.

- 이후 GPU 실습에서 S3 다운로드 구조가 어떻게 사용될 수 있는가?
  - g4dn GPU 서버에서도 같은 S3 Bucket과 Key를 사용해 학습 데이터를 다운로드할 수 있다.
  - g4dn에서 생성한 모델 파일은 artifact Prefix에 저장할 수 있다.
  - g4dn에서 생성한 실행 로그는 log Prefix에 저장할 수 있다.
  - Day 5에서 만든 S3 다운로드 구조는 이후 GPU 모델 학습 서버에서도 재사용할 수 있다.

## 10. 오늘 이해한 점

-

## 11. 다음 교시에서 할 일

데이터 검증 + 전처리 로직 재사용
