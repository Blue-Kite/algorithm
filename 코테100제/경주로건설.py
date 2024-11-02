from collections import deque
from sys import maxsize

def bfs(board, dir):
    n = len(board)
    visited = [[maxsize for _ in range(n)] for _ in range(n)]  # 방문 겸 비용 저장 
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited[0][0] = 0
    q = deque([])
    q.append([0, 0, dir, 0])  # x좌표, y좌표, 방향, 경비 

    while q:
        x, y, d, c = q.popleft()

        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                cost = c + (100 if i == d else 600)

                if visited[nx][ny] > cost:
                    visited[nx][ny] = cost
                    q.append([nx, ny, i, cost])

    return visited[n-1][n-1]

def solution(board):
    return min(bfs(board, 2), bfs(board, 1))
