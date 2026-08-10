# 문제: 알파벳 대소문자별 개수 세기
# 난이도: Lv.0

def solution(my_string):
    result = [0] * 52
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            result[ord(ch) - ord('A')] += 1
        else:
            result[26 + ord(ch) - ord('a')] += 1
    return result
