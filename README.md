# MagicSquare_1004

4×4 **부분 마방진**(빈칸 2개, 1~16, 합 34)의 **행·열·대각선 10조건**을 검증하는 프로젝트.

Mom Test(STEP 1)로 문제를 정의하고, 세션 3부터 **Rule · Command · Test Loop** 로 검증 기능을 구현한다.

---

## 문제 정의 (Mom Test)

| 항목 | 내용 |
|------|------|
| **페르소나** | 4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 학습자 |
| **진짜 문제** | 여러 조건을 맞추다 하나를 놓치면, 틀린 답을 오래 붙잡다 20분을 날린다 |
| **주제** | 10조건(행·열·대각선) 검증 누락으로 틀린 배치를 늦게 아는 문제를 줄인다 |

**표면 문제 (하지 않음):** 마방진 체커 앱·GUI·Solver·TDD 설교

---

## 도메인

```
Magic Square = 4×4, 1~16, 모든 행·열·대각선 합 = 34
과제         = 빈칸 2개(0) 위치 찾기 + 숫자 배치
검증 (10선)  = 행 4 + 열 4 + 대각선 2
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test + 주제 선정 + 범위 |
| [docs/PRD.md](docs/PRD.md) | 기능·비기능 요구사항, 성공 기준 |
| [report/01.mom-test-report.md](report/01.mom-test-report.md) | STEP 1 Mom Test 원본 보고서 |
| [prompting/01.step1-mom-test-prompt.md](prompting/01.step1-mom-test-prompt.md) | STEP 1 Mom Test 인터뷰 프롬프트 |
| [prompting/02.transcript-export.md](prompting/02.transcript-export.md) | STEP 1 인터뷰 트랜스크립트 |
| [prompting/03.mom-test-questions-bank.md](prompting/03.mom-test-questions-bank.md) | Mom Test 질문 10개 (✅/❌) |
| [prompting/04.session3-workbook-prompt.md](prompting/04.session3-workbook-prompt.md) | 세션 3 워크북 작성 프롬프트 |
| [prompting/05.mom-test-grading-prompt.md](prompting/05.mom-test-grading-prompt.md) | Mom Test 워크북 채점 프롬프트 |
| [prompting/06.report-prd-readme-prompt.md](prompting/06.report-prd-readme-prompt.md) | Report / PRD / README 생성 프롬프트 |
| [prompting/07.real-problem-to-topic-prompt.md](prompting/07.real-problem-to-topic-prompt.md) | 진짜 문제 → 주제 선정 설명 요청 |

---

## 프로젝트 구조 (예정)

```
magicsquare/
├── Report/          # 문제 정의 보고서
├── docs/            # PRD 등 설계 문서
├── report/          # Mom Test STEP 1 보고서
├── prompting/       # 인터뷰·워크북·채점·문서 생성 프롬프트 (01~07)
├── src/             # (예정) Rule, Command, Validator
└── tests/           # (예정) Test Loop
```

---

## 세션 3 구현 범위 (8계층)

| 계층 | 이번 세션 |
|------|-----------|
| Rule | ✅ 검증 규칙 (10선, 합 34) |
| Command | ✅ `validate` |
| Skill | ✅ 줄 합 검사 등 |
| Test Loop | ✅ pytest |
| Entity / Control / Boundary | ⬜ 다음 세션 |

---

## 환경 설정

```powershell
cd C:\Users\usejen_id\Desktop\magicsquare
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pytest
pytest -v
```

---

## 라이선스

교육·실습용 프로젝트.
