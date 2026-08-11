# 번호: 181897
# 문제: 리스트자르기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181897

def solution(n, slicer, num_list):
    answer = []
    if n == 1 :
        answer = num_list[0:slicer[1]+1]
    elif n == 2:
        answer = num_list[slicer[0]:]
    elif n == 3:
        answer = num_list[slicer[0]:slicer[1]+1]
    elif n == 4 :
        answer = num_list[slicer[0]:slicer[1]+1:slicer[2]]
    return answer


def solution_ai(n, slicer, num_list):
    start = 0 if n == 1 else slicer[0]
    stop = len(num_list) if n == 2 else slicer[1] + 1
    step = slicer[2] if n == 4 else 1
    return num_list[start:stop:step]