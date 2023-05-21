#아웃풋의 결과가 10억 => 하나씩 찾는 것 자체가 시간초과
#경로수를 저장해나가야함 

import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(maps, cnt, x, y):
    #방문한적이 있으면 dfs중단 
    if cnt[x][y] >= 0:
        return cnt[x][y]
    
    #방문처리 
    cnt[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #범위일 경우 
        if 0<=nx<len(maps) and 0<= ny < len(maps[0]):
            #내림막일 경우 
            if maps[x][y] > maps[nx][ny]:
                cnt[x][y] += dfs(maps, cnt, nx, ny)

    return cnt[x][y]


m, n = map(int, sys.stdin.readline().split())
maps = []
for _ in range(m):
    maps.append(list(map(int, sys.stdin.readline().split())))

#경로 수를 저장하는 배열
cnt = [[-1 for _ in range(n)] for _ in range(m)]

#dfs함수는 해당 지역를 통과해서 목적지까지 가는 경로를 반환 
#방문체크는 -1이상, 방문했지만 경로 불가능 0, 
#범위를 벗어나지 않고 내리막길이면 계속 직진 

#dp초기화
cnt[m-1][n-1] = 1

dfs(maps, cnt, 0, 0)
print(cnt[0][0])