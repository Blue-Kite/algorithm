#P와 P사이 거리가 1이상
from collections import deque
def bfs(place):
    start = []
    #사람이 있는 곳이 시작점
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i,j))
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #시작점마다 각각 bfs를 돌림
    for sx, sy in start:
        q = deque([])
        distance = [[0 for _ in range(5)] for _ in range(5)]
        visited = [[0 for _ in range(5)] for _ in range(5)]
        q.append((sx,sy))
        visited[sx][sy] = 1

        while q:
            x, y = q.popleft()
            for k in range(4):
                dx = x + direction[k][0]
                dy = y + direction[k][1]

                if 0<=dx<5 and 0<=dy<5 and not visited[dx][dy]:
                    #테이블이면 방문 
                    if place[dx][dy] == 'O':
                        q.append((dx, dy))
                        visited[dx][dy] = 1
                        distance[dx][dy] = distance[x][y] + 1
                    #사람에서 바로 사람인 경우 
                    if place[dx][dy] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer