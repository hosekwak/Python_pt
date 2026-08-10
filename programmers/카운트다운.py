# 번호: 181899
# 문제: 카운트다운
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181899

def solution_MY(start_num, end_num):
    answer = []
    for i in range(start_num,end_num-1,-1):
        answer.append(i)
    return answer

def solution_ai(start_num, end_num):
    return list(range(start_num, end_num - 1, -1))