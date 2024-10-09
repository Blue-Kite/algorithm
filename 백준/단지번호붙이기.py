import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
visited = [[0 for _ in range(n)] for _ in range(n)]
answer = 0
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
answer = []

for i in range(n):
    board.append(list(map(int, input().strip())))

def bfs(i, j):
    q = deque([])
    q.append([i, j])
    visited[i][j] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]    
            if 0<=dx<n and 0<=dy<n and not visited[dx][dy] and board[dx][dy]:
                q.append([dx, dy])
                visited[dx][dy] = 1
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            answer.append(bfs(i, j))
            cnt += 1
print(cnt)
for n in sorted(answer):
    print(n)