# 번호: 181872
# 문제: 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181872

def solution(myString, pat):
    idx = myString.rfind(pat)
    return myString[:idx + len(pat)]