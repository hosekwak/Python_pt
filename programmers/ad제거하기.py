# 번호: 181870
# 문제: ad제거하기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    return [s for s in strArr if "ad" not in s]