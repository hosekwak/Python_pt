# 번호: 181880
# 문제: 1로 만들기
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181880

def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1 :
            if i % 2 == 0 :
                i //= 2
                answer +=1
            else : i -= 1
            
    return answer