#높이는 1이상 100 이하의 정수
#이코테랑 비교해보기 

import sys
from collections import deque

n = int(sys.stdin.readline())
rain = []
maxnum = 0 
for i in range(n):
    rain.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if rain[i][j] > maxnum:
            maxnum = rain[i][j] #최대 강수량 
#비가 안 올수 있어서 0부터 maxnum-1까지 확인
dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]

def bfs(j, k, high, visited):
    q = deque()
    q.append((j,k))
    visited[j][k] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and rain[nx][ny] > high:
                q.append((nx,ny))
                visited[nx][ny] = 1



result = 0
for i in range(maxnum): 
    #강수량마다 새로 선언 
    visited = [[0] * n for i in range(n)]
    cnt = 0

    #강수량마다 bfs를 돌려 영역을 구함
    for j in range(n):
        for k in range(n):
            #bfs 할때마다 하나의 영역이 나옴 
            if rain[j][k] > i and visited[j][k] == 0:
                bfs(j,k,i,visited)
                cnt += 1

    if result < cnt:
        result = cnt
print(result)