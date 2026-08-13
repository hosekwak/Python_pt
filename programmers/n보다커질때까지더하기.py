# 번호: 181884
# 문제: n보다커질때까지더하기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    answer = 0
    for add in numbers:
        answer+=add
        if answer > n :
            break
    return answer