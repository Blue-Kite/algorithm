def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    
    while s != '1':
        new_s = '1'*(len(s) - s.count('0'))
        cnt += 1
        zero_cnt += s.count('0')
        s = bin(len(new_s))[2:]
        
    return [cnt, zero_cnt]