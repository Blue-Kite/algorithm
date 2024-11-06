#bfs로 넓이 구하기 
#정사영하기 => 같은 열이면 시추가 가능하다 
from collections import deque
        
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    result = [0 for _ in range(m)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x,y):
        q = deque()
        q.append([x, y])
        visited[x][y] = 1
        cnt = 1
        min_y = y
        max_y = y

        while q:
            dx, dy = q.popleft()
            for k in range(4):
                nx = dx + d[k][0]
                ny = dy + d[k][1]

                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1
                    min_y = min(min_y, ny)
                    max_y = max(max_y, ny)
                    
        for i in range(min_y, max_y+1):
            result[i] += cnt

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j)
                
    return max(result)