from collections import deque
def solution(maps):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque([])
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q.append([0,0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i  in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0<= nx < n and  0<= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
            

    if visited[n-1][m-1] == 0:
        return -1
    else:
        return visited[n-1][m-1]