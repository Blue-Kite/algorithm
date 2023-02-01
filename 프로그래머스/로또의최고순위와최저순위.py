#대박인 풀이 
#https://programmers.co.kr/learn/courses/30/lessons/77484/solution_groups?language=python3

def solution(lottos, win_nums):
    answer = []
    win = 0
    zero = 0

    for l in lottos:
        if l in win_nums:
            win += 1
        if l == 0:
            zero += 1

    zero = zero + win
    if 7-zero == 7: # 다틀리고 0도 없을 때 win = 0 zero = 0
        answer.append(6)
    else:
        answer.append(7-zero)
    
    if win == 0:
        win = 1
    answer.append(7-win)
    
    return answer