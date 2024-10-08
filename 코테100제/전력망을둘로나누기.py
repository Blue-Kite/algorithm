
def solution(n, wires):
    answer = -1
    graph = [[]] for _ in range(n+1)
    
    def dfs(i, j):
        cnt = 1
        for v in graph[i]:
            if v != j:
                cnt = dfs(v, i)
        return cnt

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        cnt1 = dfs(a,b)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1- cnt2))

        graph[a].append(b)
        graph[b].append(a)
        
    return answer