# 번호: 181901
# 문제: 배열 만들기 1
# 난이도: Lv.0
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181901

# MY
def solution(n, k):
    answer = []
    i = 1
    while i*k <= n:
        answer.append(i*k)
        i+=1
    return answer

# AI
def solution_AI(n, k):
    return list(range(k, n + 1, k))