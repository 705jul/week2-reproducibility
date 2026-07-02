# 2주차 Day 3 재현성 및 환경 분리 최종 리포트
## 1. 작성자
student
## 2. Day 3 주제
실험 재현성과 환경 분리
## 3. 핵심 목표
Day 3의 목표는 개인 로컬 PC에서만 실행되는 코드를 만드는 것이 아니라,
같은 저장소, 같은 requirements.txt, 같은 .env.example, 같은 src 구조,
같은 입력 데이터 기준으로 다른 환경에서도 다시 실행 가능한 구조를 만드는 것이다.
## 4. 실습 환경
| 항목 | 사용 여부 |
|---|---|
| 개인 로컬 PC WSL2 | 사용 |
| OpenShift Local | 앱 배포 없음, 동일 실행 구조만 정리 |
| Developer Sandbox | 앱 배포 없음, 동일 실행 구조만 정리 |
| AWS g4dn.xlarge | 사용하지 않음 |
| H200 | 사용하지 않음 |
## 5. 오늘 만든 핵심 구조
| 항목 | 설명 |
|---|---|
| .venv | 개인 로컬 프로젝트 전용 Python 환경 |
| requirements.txt | 패키지와 버전 기록 |
| .env.example | 공유 가능한 설정 예시 |
| .env | 개인 설정 파일, Git 제외 |
| src/seed.py | seed 고정 함수 |
| src/paths.py | 프로젝트 경로 함수 |
| src/io_utils.py | 파일 읽기/저장 함수 |
| outputs/run_info.json | 실행 조건 누적 기록 |
| README.md | 실행 방법 문서 |
## 6. OpenShift 동일 실행 구조
OpenShift Local 또는 Developer Sandbox에서는 같은 저장소를 가져온 뒤
requirements.txt로 패키지를 설치하고,
.env.example을 기반으로 환경 변수를 설정한 뒤,
src 구조를 사용해 같은 데이터 처리 코드를 실행할 수 있다.
이번 Day 3에서는 OpenShift Deployment, Service, Route를 만들지 않는다.
배포는 이후 OpenShift 배포 주차에서 수행한다.
## 7. g4dn.xlarge 연결
Day 3에서는 GPU 연산이 없으므로 g4dn.xlarge를 사용하지 않는다.
하지만 이후 GPU 실습 주차에서는 같은 저장소 구조,
requirements 파일,
.env.example,
src 구조,
run_info.json 기록 방식을 그대로 사용할 수 있다.
## 8. 최종 산출물
| 산출물 | 경로 |
|---|---|
| Day 3 Notebook | notebooks/03_reproducibility_environment.ipynb |
| requirements | requirements.txt |
| 환경 예시 | .env.example |
| seed 함수 | src/seed.py |
| 경로 함수 | src/paths.py |
| 입출력 함수 | src/io_utils.py |
| 실행 기록 | outputs/run_info.json |
| seed split 결과 | outputs/seed_split_result.json |
| 환경 변수 요약 | outputs/env_config_summary.json |
| src 테스트 결과 | outputs/src_test_info.json |
| OpenShift 동일 실행 가이드 | outputs/openshift_same_execution_guide.md |
| Day 3 최종 산출물 요약 | outputs/day3_final_artifact_summary.json |
## 9. Day 4 연결
Day 4에서는 오늘 만든 재현성 구조를 바탕으로
AWS S3 데이터 적재,
S3 Prefix 구조,
데이터 버전관리,
S3 Lifecycle,
raw/ clean/ feature/ 흐름을 다룬다.
## 10. 오늘 이해한 점
재현성은 seed 하나로 끝나지 않는다.
패키지, 경로, 환경 변수, src 구조, 실행 기록, README가 함께 있어야
다른 환경에서도 다시 실행 가능한 실험 구조가 된다.
