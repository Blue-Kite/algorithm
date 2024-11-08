def solution(lottos, win_nums):
    answer = []
    cnt = 0
    num0 = 0
    
    for i in range(6):
        for j in range(6):
            if lottos[i] == 0:
                num0 += 1
                break
            if lottos[i] == win_nums[j]:
                cnt += 1
    
    max_rank = 6 if cnt + num0 < 2 else 7-(cnt + num0)
    min_rank = 6 if cnt < 2 else 7-(cnt)
    
    return [max_rank, min_rank]