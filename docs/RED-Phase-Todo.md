# RED Phase Todo — Dual-Track TDD

**프로젝트:** MagicSquare_1004  
**Phase:** RED (실패 테스트만 · `src/` 구현 금지)  
**근거:** `.cursorrules`, `.cursor/skills/magic-square-tdd/SKILL.md`, `reference.md`, 세션 Boundary RED 설계표

---

## 공통 규칙

- [ ] RED → GREEN → REFACTOR 순서 준수 (Phase 건너뛰기 금지)
- [ ] `@pytest.mark.skip`, `xfail`, assert 완화로 RED 회피 금지
- [ ] Mom Test·PRD AC와 무관한 테스트 추가 금지
- [ ] RED 직후: `pytest <새 테스트 경로> -v` → **FAIL** 확인

---

## Boundary — UI Track

**Layer:** boundary · **Track:** UI  
**테스트 위치:** `tests/boundary/test_u_*.py`  
**검증 대상:** 입출력 형식, E001~E007, control 호출 흐름 (control Mock 허용)

### 입력 검증 (U-IN)

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:--------|:------|:--------------|:---------------------|
| U-IN-01 | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` |
| U-IN-02 | `grid=3×4` (4×4 아님) | `E001` `INVALID_SIZE` | `AssertionError` |
| U-IN-03 | 빈칸 0개 (0이 2개 아님) | `E002` `INVALID_BLANKS` | `AssertionError` |

- [ ] **U-IN-01** — `grid=None` → `E003 INVALID_NULL` (RED: `ModuleNotFoundError`)
- [ ] **U-IN-02** — `grid=3×4` → `E001 INVALID_SIZE` (RED: `AssertionError`)
- [ ] **U-IN-03** — 빈칸 0개 → `E002 INVALID_BLANKS` (RED: `AssertionError`)

### 출력 형식 (U-OUT)

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:--------|:------|:--------------|:---------------------|
| U-OUT-01 | 유효 입력 G1 | `len(result) == 6` (`int[6]` Solver 형식) | `pytest.fail()` RED |

- [ ] **U-OUT-01** — 유효 입력 G1 → `len(result) == 6` (RED: `pytest.fail()` RED)

### 흐름 (U-FLOW)

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:--------|:------|:--------------|:---------------------|
| U-FLOW-02 | `grid=None` | `execute()` 0회 호출 (control 미호출) | `pytest.fail()` RED |

- [ ] **U-FLOW-02** — `grid=None` → `execute()` 0회 호출 (RED: `pytest.fail()` RED)

### Boundary Track 완료 체크

- [ ] `tests/boundary/test_u_*.py`에 U-IN / U-OUT / U-FLOW 테스트 작성 완료
- [ ] entity 직접 import 없음 (control 경유만)
- [ ] E001~E007는 boundary에서만 정의·발행

---

## Logic — Logic Track

**Layer:** entity / control · **Track:** Logic  
**테스트 위치:** `tests/entity/`, `tests/control/`, `test_d_*.py`  
**검증 대상:** `validate` → `{ ok: bool, violations: [...] }` (E코드 없음 · Domain Mock 금지)

### Mom Test AC (필수)

| AC | Test ID | Given | Then (기대값) | Expected RED Failure |
|----|---------|:------|:--------------|:---------------------|
| AC-4 | D-001 | 10선 + 숫자 규칙 모두 만족 격자 | `ok is True`, `violations == []` | `ModuleNotFoundError` / `AssertionError` |
| AC-1 | D-002 | 대각선 1개만 검사 누락 구현 + 대각선 틀린 격자 | 반드시 실패 (`ok is False`) | `pytest.fail()` RED |
| AC-2 | D-003 | 행·열만 합 34, 대각선 틀림 | `ok is False` | `AssertionError` |
| AC-3 | D-004 | 임의 1선 위반 격자 | `violations`에 깨진 행/열/대각선 식별 | `AssertionError` |

- [ ] **D-001** (AC-4) — 전 조건 통과 → `ok is True`, `violations == []`
- [ ] **D-002** (AC-1) — 대각선 검사 누락 시나리오 → 반드시 실패
- [ ] **D-003** (AC-2) — 행·열만 34, 대각선 틀림 → `ok is False`
- [ ] **D-004** (AC-3) — 실패 시 `violations`에 위반 선 식별

### 입력·규칙 (도메인)

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:--------|:------|:--------------|:---------------------|
| D-005 | 빈칸(0) ≠ 2개 | `ok is False` | `AssertionError` |
| D-006 | 1~16 중복 또는 범위 밖 | `ok is False` | `AssertionError` |

- [ ] **D-005** — 빈칸(0) ≠ 2개 → `ok is False`
- [ ] **D-006** — 1~16 중복·범위 밖 → `ok is False`

### 10선 합 34 (행·열·대각선)

| Test ID | Given | Then (기대값) | Expected RED Failure |
|:--------|:------|:--------------|:---------------------|
| D-007 | 특정 행 합 ≠ 34 | `ok is False` + 해당 행 in `violations` | `AssertionError` |
| D-008 | 특정 열 합 ≠ 34 | `ok is False` + 해당 열 in `violations` | `AssertionError` |
| D-009 | 대각선 ↘ 합 ≠ 34 | `ok is False` | `AssertionError` |
| D-010 | 대각선 ↙ 합 ≠ 34 | `ok is False` | `AssertionError` |

- [ ] **D-007** — 행 합 ≠ 34 → 실패 + 해당 행 in `violations`
- [ ] **D-008** — 열 합 ≠ 34 → 실패 + 해당 열 in `violations`
- [ ] **D-009** — 대각선 ↘ 합 ≠ 34 → `ok is False`
- [ ] **D-010** — 대각선 ↙ 합 ≠ 34 → `ok is False`

### Logic Track 완료 체크

- [ ] `tests/**/test_d_*.py`에 D-001~D-010 작성 완료
- [ ] AC-1~AC-4 최소 커버 (D-001~D-004)
- [ ] Domain Mock (`patch`, `monkeypatch` on Validator/entity) 없음
- [ ] entity/control에서 E001~E007 문자열 발행 없음

---

## Boundary vs Logic 요약

| 항목 | Boundary (UI) | Logic |
|------|---------------|-------|
| 테스트 ID | `U-*` | `D-*` |
| 실패 표현 | E001~E007 | `ok` / `violations` |
| Mock | control Mock 허용 | Domain Mock 금지 |
| v0.1 핵심 출력 | E코드, `int[6]`, 호출 횟수 | `{ ok, violations }` |

---

## Phase 완료 (Review)

- [ ] Boundary RED: U-IN-01~03, U-OUT-01, U-FLOW-02 각각 `pytest` **FAIL** 확인
- [ ] Logic RED: D-001~D-010 각각 `pytest` **FAIL** 확인
- [ ] 다음 Phase: **GREEN** — RED를 통과시키는 최소 `src/` 구현 (별도 Todo)

---

## 참고

- [PRD.md](./PRD.md) — FR-004·FR-005, AC-1~4
- [.cursor/skills/magic-square-tdd/reference.md](../.cursor/skills/magic-square-tdd/reference.md) — D-* ID SSOT
- [Report/01.MagicSquare_ProblemDefinition_Report.md](../Report/01.MagicSquare_ProblemDefinition_Report.md) — Mom Test·실패 조건
