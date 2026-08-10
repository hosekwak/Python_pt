# 문제: 부분 문자열 정수 변환
# 난이도: Lv.1

def solution(intStrs, k, s, l):
    return [num for num in (int(str_[s:s + l]) for str_ in intStrs) if num > k]
