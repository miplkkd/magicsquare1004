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
| [docs/RED-Phase-Todo.md](docs/RED-Phase-Todo.md) | Dual-Track RED 단계 설계표·Todo (SSOT) |
| [report/02.RED_D-LOC-01_Session_Report.md](report/02.RED_D-LOC-01_Session_Report.md) | RED 세션 보고서 (D-LOC-01) |
| [report/03.GREEN_D-LOC-01_Session_Report.md](report/03.GREEN_D-LOC-01_Session_Report.md) | GREEN 세션 보고서 (D-LOC-01) |
| [prompting/08.transcript-red-d-loc-01-export.md](prompting/08.transcript-red-d-loc-01-export.md) | RED D-LOC-01 세션 트랜스크립트 |
| [prompting/09.transcript-green-d-loc-01-export.md](prompting/09.transcript-green-d-loc-01-export.md) | GREEN D-LOC-01 세션 트랜스크립트 |
| [report/04.Golden_Master_D-SOL-01_Session_Report.md](report/04.Golden_Master_D-SOL-01_Session_Report.md) | Golden Master 세션 보고서 (D-SOL-01) |
| [prompting/10.transcript-golden-d-sol-01-export.md](prompting/10.transcript-golden-d-sol-01-export.md) | Golden Master D-SOL-01 트랜스크립트 |
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

## RED Phase 체크리스트

상세 설계표(Given / Then / Expected RED Failure)는 [docs/RED-Phase-Todo.md](docs/RED-Phase-Todo.md)를 참고한다.  
**규칙:** 실패 테스트만 작성 · `src/` 구현 금지 · RED 직후 `pytest`로 **FAIL** 확인.

### 공통

- [ ] RED → GREEN → REFACTOR 순서 준수
- [ ] `skip` / `xfail` / assert 완화로 RED 회피하지 않음
- [ ] Mom Test·PRD AC와 무관한 테스트 추가하지 않음

### Boundary — UI Track (`tests/boundary/test_u_*.py`)

**입력 검증 (U-IN)**

- [ ] **U-IN-01** — `grid=None` → `E003 INVALID_NULL`
- [ ] **U-IN-02** — `grid=3×4` → `E001 INVALID_SIZE`
- [ ] **U-IN-03** — 빈칸 0개 → `E002 INVALID_BLANKS`

**출력·흐름**

- [ ] **U-OUT-01** — 유효 입력 G1 → `len(result) == 6`
- [ ] **U-FLOW-02** — `grid=None` → `execute()` 0회 호출

**Track 완료**

- [ ] U-IN / U-OUT / U-FLOW 테스트 파일 작성 완료
- [ ] entity 직접 import 없음 (control 경유)
- [ ] E001~E007는 boundary에서만 정의·발행

### Logic — Logic Track (`tests/entity/`, `tests/control/`, `test_d_*.py`)

**Mom Test AC (필수)**

- [ ] **D-001** (AC-4) — 전 조건 통과 → `ok is True`, `violations == []`
- [ ] **D-002** (AC-1) — 대각선 검사 누락 시나리오 → 반드시 실패
- [ ] **D-003** (AC-2) — 행·열만 34, 대각선 틀림 → `ok is False`
- [ ] **D-004** (AC-3) — 실패 시 `violations`에 위반 선 식별

**입력·규칙**

- [ ] **D-005** — 빈칸(0) ≠ 2개 → `ok is False`
- [ ] **D-006** — 1~16 중복·범위 밖 → `ok is False`

**10선 합 34**

- [ ] **D-007** — 행 합 ≠ 34 → 실패 + 해당 행 in `violations`
- [ ] **D-008** — 열 합 ≠ 34 → 실패 + 해당 열 in `violations`
- [ ] **D-009** — 대각선 ↘ 합 ≠ 34 → `ok is False`
- [ ] **D-010** — 대각선 ↙ 합 ≠ 34 → `ok is False`

**Track 완료**

- [ ] D-001~D-010 테스트 파일 작성 완료
- [ ] Domain Mock 없음 (`patch` / `monkeypatch` on Validator·entity 금지)
- [ ] entity/control에서 E001~E007 문자열 발행 없음

### RED Phase Review

- [ ] Boundary: U-IN-01~03, U-OUT-01, U-FLOW-02 — 각각 `pytest` **FAIL** 확인
- [ ] Logic: D-001~D-010 — 각각 `pytest` **FAIL** 확인
- [ ] 다음: **GREEN** — 최소 `src/` 구현으로 위 테스트 통과

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
