# 번호: 181900
# 문제: 글자지우기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181900

#MY
def solution(my_string, indices):
    s = set(indices)
    result = ""
    for i in range(len(my_string)):
        if i not in s:
            result += my_string[i]
    return result

#AI
def solution(my_string, indices):
    return "".join(ch for i, ch in enumerate(my_string) if i not in set(indices))