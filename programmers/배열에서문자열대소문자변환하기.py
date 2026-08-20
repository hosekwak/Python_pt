# 번호: 181875
# 문제: 배열에서 문자열 대소문자 변환하기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181875

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 1:
            answer.append(str.upper(strArr[i]))
        else :
            answer.append(str.lower(strArr[i]))
    return answer