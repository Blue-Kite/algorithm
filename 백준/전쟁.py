from collections import deque 

n, m = map(int, input().split())
board = []
direction = [(0,-1), (1, 0), (0, 1), (-1, 0)]

for _ in range(m):
    board.append(list(input()))

def bfs(x, y, st, visited):
    cnt = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        dx, dy = q.popleft()
        for k in range(4):
            nx, ny = dx + direction[k][0] , dy + direction[k][1]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == st:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    print(x,y, cnt)
    return cnt**2

result = []
std = ['W', 'B']
for k in range(2):
    cnt = 0 
    visited = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and board[i][j] == std[k]:
                cnt += bfs(i, j, std[k], visited)
    result.append(cnt)

print(result[0], result[1])