# 번호: 181890
# 문제: 왼쪽오른쪽
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181890

def solution(str_list):
    for i, c in enumerate(str_list):
        if c == 'l':
            return str_list[:i]
        if c == 'r':
            return str_list[i + 1:]
    return []