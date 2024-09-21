def solution(N, stages):
    answer = {}
    user = len(stages)
    fail = [0 for _ in range(N+2)]
    for stage in stages:
        fail[stage] += 1
    
    for i in range(1, N+1):
        if fail[i] == 0:
            answer[i] = 0
        else:
            answer[i] = fail[i] / user
            user -= fail[i]
    #딕셔너리 정렬
    answer = sorted(answer, key=lambda x : answer[x], reverse=True)
    return answer