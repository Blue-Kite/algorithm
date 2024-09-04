from collections import deque
import sys
input = sys.stdin.readline

l, w = map(int, input().split())
graph = []
for _ in range(l):
    graph.append(list(input().rstrip()))
    
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * w for _ in range(l)]
    visited[x][y] = 0
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < w and visited[nx][ny] == -1:
                if graph[nx][ny] == "L":
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
    return cnt

treasure = 0
for i in range(l):
    for j in range(w):
        if graph[i][j] == 'L':
            treasure = max(treasure, bfs(i, j))

print(treasure)