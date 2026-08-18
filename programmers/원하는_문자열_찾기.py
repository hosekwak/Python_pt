# 번호: 181878
# 문제: 원하는 문자열 찾기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    answer = 0
    if str.lower(pat) in str.lower(myString) : 
        answer = 1
    else :
        answer = 0
    return answer