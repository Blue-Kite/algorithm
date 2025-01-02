#네트워크 개수 => 끝까지 파고들어서 몇개인지 알아야함 

def dfs(n, i, computers, visited):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            dfs(n, j, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(n, i, computers, visited)
            answer += 1

    return answer