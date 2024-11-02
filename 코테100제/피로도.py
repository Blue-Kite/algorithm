def dfs(k, cnt, visited, dungeons):
    max_cnt = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            max_cnt = max(max_cnt, dfs(k-dungeons[i][1], cnt+1, visited, dungeons))
            visited[i] = 0 #부모의 형제들도 방문할 수 있도록 
    
    return max_cnt

def solution(k, dungeons):
    n = len(dungeons)
    visited = [0 for _ in range(n)]
    cnt = 0 # 유저가 방문한 던전 수 
    answer = dfs(k, cnt, visited, dungeons) 
    return answer