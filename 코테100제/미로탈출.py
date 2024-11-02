#최단거리 bfs
from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    s_x, s_y, e_x, e_y = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s_x, s_y = i, j
            if maps[i][j] == 'E':
                e_x, e_y = i, j 
    
    q = deque([])
    #x좌표, y좌표, 레버 당김여부, 최단거리 
    #레버를 당겼는지 여부에 따른 방문은 분리 
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    q.append([s_x, s_y, False, answer])
    visited[s_x][s_y][0] = 1 
    direction = [(-1,0), (0, 1), (1, 0), (0, -1)]
    
    while q:
        x, y, k, cost = q.popleft()
        print(x,y,k,cost)
        
        if x == e_x and y == e_y and k:
            return cost
        
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] != 'X':
                if maps[nx][ny] == 'L':
                    if not visited[nx][ny][1]: 
                        q.append([nx, ny, 1, cost +1])
                        visited[nx][ny][1] = 1
                else:
                    if not visited[nx][ny][k]: 
                        q.append([nx, ny, k, cost+1])
                        visited[nx][ny][k] = 1
    return -1