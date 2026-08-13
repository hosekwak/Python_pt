# 번호: 181887
# 문제: 홀수 vs 짝수
# 난이도: Lv.0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181887

def solution(num_list):
    odd = 0
    even = 0
    for i in range(len(num_list)):
        if i % 2 == 0 :
            even += num_list[i]
        else :
            odd += num_list[i]
            
    return even if even > odd else odd


def solution_ai(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))