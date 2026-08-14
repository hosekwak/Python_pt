# 번호: 181882
# 문제: 조건에 맞게 수열 변환하기 1
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181882

def solution(arr):
    answer = []
    for i, n in enumerate(arr):
        if n >= 50 and n%2 == 0:
            arr[i] = n / 2
        elif n < 50 and n%2 != 0:
            arr[i] = n * 2
    return arr

def solution_ai(arr):
    return [n // 2 if n >= 50 and n % 2 == 0 else n * 2 if n < 50 and n % 2 != 0 else n for n in arr]