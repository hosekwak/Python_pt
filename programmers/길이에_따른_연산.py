# 번호: 181879
# 문제: 길이에 따른 연산
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181879

from math import prod

from math import prod

def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(n for n in num_list)
    elif len(num_list) <= 10 : answer = prod(n for n in num_list)
        
    return answer


from math import prod

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)