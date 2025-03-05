def solution(players, m, k):
    answer = 0
    t = len(players)
    server = [0] * t #i시 기준으로 총 증설된 서버 수

    def expand_server(need_server, idx):
        for i in range(k):
            if idx+i < t:
                server[idx+i] += need_server
        
    for idx, p in enumerate(players):
        need_server = (p // m) - server[idx] 
        if need_server > 0:
            expand_server(need_server, idx)
            answer += need_server
    return answer
    