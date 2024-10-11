n = int(input())
tree = [[] for _ in range(n+1)]
answer = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    tree[a].append(a)
    tree[b].append(b)

def dfs(node, prev):
    answer[node] = prev
    for nxt in tree[node]:
        if prev != nxt:
            dfs(nxt, node)
dfs(1, 0)
