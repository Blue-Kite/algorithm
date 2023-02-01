#dfs 풀이 https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94

import sys
from collections import deque
t = int(sys.stdin.readline())
answer = []
dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]

def bfs(i, j,m,n, ground):
    q = deque()
    q.append((i, j))
    ground[i][j] = 0 #방문처리

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and ground[nx][ny] == 1:
                q.append((nx, ny)) 
                ground[nx][ny] = 0

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    ground = [[0]*n for _ in range(m)]
    cnt = 0 
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        ground[x][y] = 1

    for i in range(m):
        for j in range(n):
            #배추영역 => 0으로 바꾸면서 영역확인 
            if ground[i][j] == 1:
                bfs(i,j, m, n, ground)
                cnt += 1
    
    print(cnt)



    