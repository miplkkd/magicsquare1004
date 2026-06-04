# MagicSquare_1004

4×4 **부분 마방진**(빈칸 2개, 1~16, 합 34)의 **행·열·대각선 10조건**을 검증하는 프로젝트.

Mom Test(STEP 1)로 문제를 정의하고, **Dual-Track TDD**(Logic / UI)와 **ECB** 계층으로 검증·Solver 기능을 구현한다.

**원격 저장소:** https://github.com/miplkkd/magicsquare1004

---

## 문제 정의 (Mom Test)

| 항목 | 내용 |
|------|------|
| **페르소나** | 4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 학습자 |
| **진짜 문제** | 여러 조건을 맞추다 하나를 놓치면, 틀린 답을 오래 붙잡다 20분을 날린다 |
| **주제** | 10조건(행·열·대각선) 검증 누락으로 틀린 배치를 늦게 아는 문제를 줄인다 |

**표면 문제 (하지 않음):** 마방진 체커 앱·GUI·풀스택 Solver·TDD 설교

---

## 도메인

```
Magic Square = 4×4, 1~16, 모든 행·열·대각선 합 = 34
과제         = 빈칸 2개(0) 위치 찾기 + 숫자 배치
검증 (10선)  = 행 4 + 열 4 + 대각선 2
Solver 출력  = int[6] → [r1, c1, n1, r2, c2, n2] (1-index)
```

상수 SSOT: `src/entity/constants.py` (`34`, `16`, `4`, 빈칸 `2`, `BLANK_CELL`)

---

## TDD 진행 현황 (Logic · entity)

| Test ID | Phase | 내용 | 상태 |
|---------|-------|------|------|
| **D-LOC-01** | RED → GREEN | `find_blank_coords` → G1 `[(2,2),(3,3)]` | ✅ |
| **D-SOL-01** | GREEN + Golden | `solve_step_a` → `int[6]` + `tests/golden/…approved.txt` | ✅ |
| **conftest** | REFACTOR | `grid_g1` — `BLANK_CELL` SSOT | ✅ |
| D-001 ~ D-010 | — | `validate` / 10선 (Mom Test AC) | ⬜ |
| U-IN / U-OUT / U-FLOW | — | Boundary (UI Track) | ⬜ |

```powershell
python -m pytest tests/ -v
# 2 passed (entity)
```

---

## 프로젝트 구조

```
magicsquare/
├── Report/                 # 문제 정의 (대문자)
├── report/                 # 세션 보고서 02~05
├── docs/                   # PRD, RED-Phase-Todo
├── prompting/              # 프롬프트·트랜스크립트 01~11
├── src/
│   ├── entity/             # constants, blank_loc, solver_step
│   ├── control/            # (예정) SquareValidator
│   └── boundary/           # (예정) GridUI, E001~E007
└── tests/
    ├── conftest.py         # G1 fixture (grid_g1)
    ├── _approval.py        # Golden Master 헬퍼
    ├── golden/             # *.approved.txt
    ├── entity/             # test_d_loc_01, test_d_sol_01
    ├── control/            # (예정) test_d_*.py
    └── boundary/           # (예정) test_u_*.py
```

---

## 문서

### 설계·요구사항

| 문서 | 설명 |
|------|------|
| [Report/01.MagicSquare_ProblemDefinition_Report.md](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test + 주제 선정 + 범위 |
| [docs/PRD.md](docs/PRD.md) | 기능·비기능 요구사항, 성공 기준 |
| [docs/RED-Phase-Todo.md](docs/RED-Phase-Todo.md) | Dual-Track RED 설계표·Todo (SSOT) |
| [report/01.mom-test-report.md](report/01.mom-test-report.md) | STEP 1 Mom Test 원본 |

### 세션 보고서 (`report/`)

| 문서 | Phase |
|------|-------|
| [02.RED_D-LOC-01](report/02.RED_D-LOC-01_Session_Report.md) | RED |
| [03.GREEN_D-LOC-01](report/03.GREEN_D-LOC-01_Session_Report.md) | GREEN |
| [04.Golden_Master_D-SOL-01](report/04.Golden_Master_D-SOL-01_Session_Report.md) | Golden Master |
| [05.REFACTOR_Conftest_BLANK_CELL](report/05.REFACTOR_Conftest_BLANK_CELL_Session_Report.md) | REFACTOR |

### 트랜스크립트 (`prompting/`)

| 문서 | 세션 |
|------|------|
| [08.red-d-loc-01](prompting/08.transcript-red-d-loc-01-export.md) | RED D-LOC-01 |
| [09.green-d-loc-01](prompting/09.transcript-green-d-loc-01-export.md) | GREEN D-LOC-01 |
| [10.golden-d-sol-01](prompting/10.transcript-golden-d-sol-01-export.md) | Golden Master |
| [11.refactor-conftest](prompting/11.transcript-refactor-conftest-export.md) | REFACTOR |
| [01~07](prompting/01.step1-mom-test-prompt.md) | Mom Test · 워크북 · 채점 프롬프트 |

---

## 세션 3 · 8계층

| 계층 | 상태 | 비고 |
|------|------|------|
| Rule / Command / Skill | ✅ (문서·설계) | `validate`, 10선 |
| Test Loop | ✅ | pytest, Golden Master |
| **Entity** | 🔜 진행 중 | `find_blank_coords`, `solve_step_a` |
| Control | ⬜ | SquareValidator |
| Boundary | ⬜ | E001~E007, U-* |

---

## RED Phase 체크리스트 (잔여)

완료: **D-LOC-01** RED/GREEN, **D-SOL-01** GREEN+Golden, conftest REFACTOR.  
상세 설계표: [docs/RED-Phase-Todo.md](docs/RED-Phase-Todo.md)

### Boundary — UI Track

- [ ] U-IN-01 ~ 03, U-OUT-01, U-FLOW-02
- [ ] `tests/boundary/test_u_*.py`

### Logic — Mom Test AC · 10선

- [ ] D-001 ~ D-010 (`validate`, `violations`)
- [ ] D-001~D-010 RED → GREEN

---

## 환경 설정

```powershell
cd C:\Users\usejen_id\Desktop\magicsquare
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pytest
python -m pytest tests/ -v
```

### Golden Master 갱신 (승인 후)

```powershell
$env:UPDATE_GOLDEN="1"
python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v
Remove-Item Env:UPDATE_GOLDEN -ErrorAction SilentlyContinue
```

---

## Git 브랜치 (참고)

| 브랜치 | 내용 |
|--------|------|
| `red` | RED 스켈레톤, RED-Phase-Todo, D-LOC-01 RED |
| `green` | GREEN, Golden Master, REFACTOR, 세션 보고서 03~05 |

---

## 라이선스

교육·실습용 프로젝트.
