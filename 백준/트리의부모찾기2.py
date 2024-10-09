import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
visited[1] = True

for _ in range(n-1):
    s,e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(v, visited):
    for e in tree[v]:
        if not visited[e]:
            answer[e] = v
            visited[e] = True
            dfs(e, visited)
dfs(1, visited)
for i in range(2, n+1):
    print(answer[i])