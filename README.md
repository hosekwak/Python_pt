<p align="center">
  <img src="https://www.python.org/static/img/python-logo.png" alt="Python logo" width="220">
</p>

# Python 코딩테스트 연습

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Update README](https://github.com/hosekwak/Python_pt/actions/workflows/update-readme.yml/badge.svg)](https://github.com/hosekwak/Python_pt/actions/workflows/update-readme.yml)

파이썬으로 프로그래머스 코딩테스트 문제를 풀며 기록하는 저장소입니다.

---

## 폴더 구조

```
Python_pt/
├── programmers/          # 프로그래머스 문제 풀이
├── scripts/
│   └── update_readme.py  # README 풀이 기록 표 자동 생성 스크립트
└── README.md
```

## 새 문제 등록 방법

`programmers/` 폴더에 풀이 파일을 추가할 때, 파일 맨 위에 아래 형식으로 메타데이터 주석을 답니다.

```python
# 번호: 12345
# 문제: 두 수의 합
# 난이도: Lv.1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12345

def solution(a, b):
    return a + b
```

이 파일을 커밋하고 `main` 브랜치로 push하면 **GitHub Actions가 자동으로** 아래 풀이 기록 표를 갱신하고 다시 커밋해줍니다. 표는 직접 수정할 필요가 없습니다.

## 풀이 기록

<!-- SOLUTIONS_TABLE_START -->
**총 9문제 풀이**
| 번호 | 문제 | 난이도 | 풀이 |
|:---:|---|:---:|:---:|
| 181893 | [배열조각하기](https://school.programmers.co.kr/learn/courses/30/lessons/181893) | Lv.0 | [코드](programmers/배열_조각하기.py) |
| 181894 | [2의영역](https://school.programmers.co.kr/learn/courses/30/lessons/181894) | Lv.0 | [코드](programmers/2의_영역.py) |
| 181895 | [배열만들기 3](https://school.programmers.co.kr/learn/courses/30/lessons/181895) | Lv.0 | [코드](programmers/배열_만들기_3.py) |
| 181896 | [첫번째로_나오는_음수](https://school.programmers.co.kr/learn/courses/30/lessons/181896) | Lv.0 | [코드](programmers/첫번째로_나오는_음수.py) |
| 181897 | [리스트자르기](https://school.programmers.co.kr/learn/courses/30/lessons/181897) | Lv.0 | [코드](programmers/리스트_자르기.py) |
| 181898 | [가까운_1_찾기](https://school.programmers.co.kr/learn/courses/30/lessons/181898) | Lv.0 | [코드](programmers/가까운_1_찾기.py) |
| 181899 | [카운트다운](https://school.programmers.co.kr/learn/courses/30/lessons/181899) | Lv.0 | [코드](programmers/카운트다운.py) |
| 181900 | [글자지우기](https://school.programmers.co.kr/learn/courses/30/lessons/181900) | Lv.0 | [코드](programmers/글자지우기.py) |
| 181901 | [배열 만들기 1](https://school.programmers.co.kr/learn/courses/30/lessons/181901) | Lv.0 | [코드](programmers/배열_만들기_1.py) |
<!-- SOLUTIONS_TABLE_END -->

## 규칙

- 문제를 풀 때는 우선 스스로 풀어본 뒤, 막히면 힌트나 다른 풀이를 참고합니다.
- 풀이에는 간단한 접근 방식(시간복잡도, 사용한 자료구조 등)을 주석이나 커밋 메시지로 남깁니다.
- 같은 문제를 더 나은 방식으로 다시 풀었다면 파일을 덮어쓰지 않고 `_v2` 등을 붙여 남겨둡니다.

## 진행 현황

- 시작일: 2026-08-10
- 목표: 매일 1문제 이상 풀기
