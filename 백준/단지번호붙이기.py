#220511
#백준 2667 단지번호붙이기
#https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())
board = []
apart = []
count = 0

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1 ,0, 0]
dy = [0, 0, -1, 1]

que = deque()
que.apped(board[0][0])
for i in range(n):
    for j in range(n):
        d = 1
