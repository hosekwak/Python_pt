# 번호: 181893
# 문제: 배열조각하기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr = arr[:q + 1]  # q번 인덱스까지 남기고 뒤를 버림
        else:
            arr = arr[q:]      # q번 인덱스부터 남기고 앞을 버림
    return arr