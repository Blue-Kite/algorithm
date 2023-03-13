#100*100 인 배열이라서 시간복잡도가 o(n^2)이면 간당간당함 
#0은 벽이고 1은 이동이 불가능
#최단거리문제 
#처음에 (1, 1) 위치에 있으며 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치

from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0,0))

    limit_x = len(maps)
    limit_y = len(maps[0])
    visited = [[0] * limit_y for i in range(limit_x)]
    dist = [[0] * limit_y for i in range(limit_x)] #dist[x][y]는 x,y지점까지 최단거리를 저장함.
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < limit_x and 0<= ny < limit_y and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1

    if dist[limit_x-1][limit_y-1] == 0:
        return -1
    else:
        return dist[limit_x-1][limit_y-1]