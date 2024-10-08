import math
def dfs(graph, visited, i, j):
        cnt = 1
        visited[j] = True

        for v in graph[j]:
            if not visited[v]:
                cnt += dfs(graph, visited, j, v)
        return cnt
    
def solution(n, wires):
    answer = math.inf
    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        visited = [False] * (n+1)
        visited[a] = True

        cnt1 = dfs(graph, visited, a,b)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1- cnt2))

        graph[a].append(b)
        graph[b].append(a)
        
    return answer