from collections import deque 
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))

visited = [[0 for _ in range(m)] for _ in range(n)]
direction = [(-1,0),(0,1), (1,0), (0, -1)]
q = deque([])
q.append([0,0])
visited[0][0] = 1

while q:
    dx, dy = q.popleft()
    for k in range(4):
        nx, ny = dx + direction[k][0], dy+direction[k][1]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 1:
            q.append([nx, ny])
            visited[nx][ny] = visited[dx][dy] + 1


print(visited[n-1][m-1])