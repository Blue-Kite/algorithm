import deque from collections

n, m = map(int, input().split())
board = []

def bfs(x, y, std):
    result = 0
    q = 
    return result

for _ in range(m):
    board.append(list(input()))

start = []
flag = False
for i in range(m):
    for j in range(n):
        if board[i][j] == 'B':
            start.append([i,j])
            flag = True
            break
    if flag:
        break
            
flag = False
for i in range(m):
    for j in range(n):
        if board[i][j] == 'W':
            start.append([i,j])
            flag = True
            break
    if flag:
        break

result = []
std = ['B', 'W']
for i in range(2):
    x, y = start[i]
    cnt = bfs(x, y, std[i])
    result.append(cnt)

print(result[0], result[1])
