from itertools import combinations_with_replacement
from collections import Counter

def calc(info, com_cnt):
    score1, score2 = 0, 0 #라이언 어피치 
    for i in range(11):
        if info[10 - i] < com_cnt.count(i): #특정키의 값 
            score1 += i
        elif info[10 - i] > 0:
            score2 += i
    return score1, score2
        
    
def solution(n, info):
    answer = [0 for _ in range(11)]
    max_diff, max_com = 0, [0] * 11
    #n발이 각각 어느 점수를 얻었는지 
    for com in combinations_with_replacement(range(0, 11), n):
        com_cnt = Counter(com)
        score1, score2 = calc(info, com)
        diff = score1 - score2 
        if max_diff < diff:
            max_diff = diff
            max_com = com_cnt 
            
    if max_diff > 0:
        for c in max_com:
            answer[10-c] = max_com[c]
        return answer
    else:
        return [-1]