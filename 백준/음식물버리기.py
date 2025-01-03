from collections import deque
n, m, k = map(int, input().split())
trash = []
for _ in range(k):
    trash.append(list(map(int, input().split())))

board = [[0 for _ in range(m+1)] for _ in range(n+1)]
for t in trash:
    i,j = t
    board[i][j] = 1

result = 0
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(i, j, visited):
    q = deque([])
    q.append([i,j])
    visited[i][j] = 1
    cnt = 1

    while q: 
        dx, dy = q.popleft()
        for k in range(4):
            nx, ny = dx+direction[k][0] , dy+direction[k][1]
            if 0<=nx<=n and 0<=ny<=m and not visited[nx][ny] and board[nx][ny] == 1:
                q.append([nx,ny])
                cnt += 1
                visited[nx][ny] = 1
    return cnt 

for t in trash:
    i, j = t
    if not visited[i][j]:
        result = max(result, bfs(i,j, visited))
print(result)