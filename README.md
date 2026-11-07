# ⚠️ **THIS IS A PLAYGROUND REPOSITORY** ⚠️

이 저장소는 GitHub의 다양한 기능(Actions, Issues, Pull Requests, Releases, Wiki 등)을 자유롭게 **시도, 실험, 연습**하기 위한 Playground입니다.

## 프로젝트 소개

이 프로젝트는 연습용 Python Web Application(FastAPI)으로 구성되어 있으며, 아래와 같은 목적으로 사용합니다.

- GitHub Actions 워크플로우 실행 실험
- 이슈/PR 생성 및 리뷰 흐름 연습
- 릴리스, 태그, 브랜치 전략 테스트
- 문서 및 협업 프로세스 점검

## 로컬 실행 방법

### 1) 가상환경 생성 및 활성화

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2) 의존성 설치

```bash
pip install -r requirements.txt
```

### 3) 서버 실행

```bash
uvicorn main:app --reload
```

### 4) 확인

- 앱 루트: `http://127.0.0.1:8000/`
- 헬스체크: `http://127.0.0.1:8000/health`
- API 문서(Swagger): `http://127.0.0.1:8000/docs`

## 제공 API

- `GET /` : Playground 방문 환영 메시지
- `GET /health` : 서버 상태 확인
- `GET /random-number` : 테스트용 랜덤 숫자 반환
- `GET /echo?message=...` : 전달한 메시지 에코

## 테스트

의존성을 설치한 뒤 CI와 같은 검사를 실행합니다.

```bash
python -m compileall main.py
pytest -q
```

## 향후 GitHub 연습 아이디어

- GitHub Actions 워크플로우 확장 (lint/test/build/deploy 분리)
- Issue / PR 템플릿 생성 및 점검
- CODEOWNERS 및 리뷰 정책 실험
- Release Drafter 또는 자동 릴리스 노트 실습
- Wiki/Project/Discussions 협업 흐름 테스트
