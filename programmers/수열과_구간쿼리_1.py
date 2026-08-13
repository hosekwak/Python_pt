# 번호: 181883
# 문제: 수열과 구간쿼리
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181883

def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr