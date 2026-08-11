# 번호: 181894
# 문제: 2의영역
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181894

def solution(arr):
    positions = [i for i, v in enumerate(arr) if v == 2]
    if not positions:
        return [-1]
    if len(positions) == 1:
        return [2]
    return arr[positions[0]:positions[-1] + 1]