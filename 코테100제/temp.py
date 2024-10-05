from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    q = deque([])
    q.append([0, 0])
    visited[0][0] = 1 #방문처리

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    if visited[n-1][m-1] == 0:
        return -1
    else:
        return visited[n-1][m-1]