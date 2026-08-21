# 번호: 181871
# 문제: 문자열이 몇 번 등장하는지 세기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181871

def solution(myString, pat):
    count = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i + len(pat)] == pat:
            count += 1
    return count