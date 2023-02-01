#삼성sw문제1
#풀이순서
#벽을 세울 수 있는 3개 지점의 모든 조합 찾기
#앞서 정한 지점에 벽을 세우고 바이러스 전파
#가장 넓은 안전지대의 범위 출력

#https://heytech.tistory.com/368

from itertools import combinations
import sys
import copy
from collections import deque

def bfs(board, empty):
    dx = [0, 0 , 1, -1]
    dy = [1, -1, 0, 0]
    buck = 3
    answer = 0

    n = len(board_new)
    m = len(board_new[0])

    #벽을 세울 좌표 3가지 
    for em in combinations(empty, buck):
        board_new = copy.deepcopy(board)
        #3곳에 벽을 세움 
        for x_w, y_w in em:
            board_new[x_w][y_w] = 1
        n = len(board_new)
        m = len(board_new[0])
    
        # 바이러스 위치
        virus = [(i, j) for i in range(n) for j in range(m) if board_new[i][j] == 2]

        # 바이러스마다 전파 끝날 때까지 반복
        while virus:
            x_v, y_v = virus.pop()
            for k in range(4):
                nx = x_v + dx[k]
                ny = y_v + dy[k]
                if 0 <= nx < n and 0 <= ny < m and board_new[nx][ny] == 0:
                    board_new[nx][ny] = 2
                    virus.append((nx, ny)) # 바이러스 전파
        
        #안전한 공간 크기 
        cnt = 0             
        for row in board_new:
            cnt += row.count(0)
        answer = max(answer, cnt)
    return answer           

n, m = map(int, sys.stdin.readline().split())
board = []
answer = 0 
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
#벽을 세울수 있는 모든 조합, 연구소크기가 최대 8*8=64이라서 복잡도에 안걸림
empty = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
answer = bfs(board, empty)
print(answer)
