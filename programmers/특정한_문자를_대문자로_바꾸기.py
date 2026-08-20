# 번호: 181873
# 문제: 특정한 문자를 대문자로 바꾸기
# 난이도: Lv.0
# 링크: http://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    answer = ''
    return ''.join(str.upper(c) if c in alp else c for c in my_string)