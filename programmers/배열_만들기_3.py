# 번호: 181895
# 문제: 배열만들기 3
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181895

def solution(arr, intervals):
    answer = []
    for (a,b) in intervals:
        answer+=(arr[a:b+1])
    return answer