# 번호: 181885
# 문제: 할 일 목록
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181885

def solution(todo_list, finished):
    answer = []
    for t, f in zip(todo_list, finished):
        if not f:
            answer.append(t)
    return answer