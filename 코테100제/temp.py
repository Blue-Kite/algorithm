def dfs(n, computers, i, visited):
    visited[i] = 1
    for j in range(n):
        if computers[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(n, computers, j, visited) 

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, i, visited)
            answer += 1

    return answer