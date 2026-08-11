# 번호: 181896
# 문제: 첫번째로_나오는_음수
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181896

def solution(num_list):
    answer = 0
    for i ,n in enumerate(num_list):
        if n < 0:
            return i
        
    return -1


def solution(num_list):
    return next((i for i, n in enumerate(num_list) if n < 0), -1)

