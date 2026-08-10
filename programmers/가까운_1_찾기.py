# 번호: 181898
# 문제: 가까운_1_찾기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181898

def solution(arr, idx):
    answer = 0
    for i , arr in enumerate(arr):
        if arr == 1 and i >= idx:
            return i
    
    return -1

def solution_ai(arr, idx):
    return next((i for i in range(idx, len(arr)) if arr[i] == 1), -1)