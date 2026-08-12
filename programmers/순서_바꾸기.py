# 번호: 181891
# 문제: 순서바꾸기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181891

def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    return answer