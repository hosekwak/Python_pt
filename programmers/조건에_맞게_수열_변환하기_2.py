# 번호: 181881
# 문제: 조건에 맞게 수열 변환하기 2
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(arr):
    def step(a):
        return [
            n // 2 if n >= 50 and n % 2 == 0
            else n * 2 + 1 if n < 50 and n % 2 != 0
            else n
            for n in a
        ]

    cur = arr
    x = 0
    while True:
        nxt = step(cur)
        if nxt == cur:
            return x
        cur = nxt
        x += 1