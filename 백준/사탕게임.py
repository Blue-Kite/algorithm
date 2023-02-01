#첫번째 풀이 
from collections import deque

def bfs(oriboard):
    maxcandy = 0
    dx = [0, 0, -1, +1]
    dy = [-1, +1, 0, 0]
    board = oriboard
    que = deque()
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: #지나간 영역 
                continue
            else:
                que.append((i,j))
                board[i][j] = 0
                count = 0
                while que:
                    count += 1
                    x, y = que.popleft()
                    for k in range(4): #4가지 방향
                        if 0<= x+dx[k] <n and 0<=y+dy[k] <n:
                            que.append((x+dx[k], y+dy[k])) #큐에 넣음
                            board[x+dx[k]][y+dy[k]] = 0 #방문체크

            maxcandy = max(maxcandy, count)
    return maxcandy

n = int(input())
board = []
for i in range(n): # list(문자열) -> [한글자씩]
    board.append(list(input()))
result = 0

for i in range(n):
    for j in range(n):
        dx = i+1
        dy = j+1

        if 0<=dx and dx<n:
            temp = board[i][j]
            board[i][j] = board[dx][j] 
            board[dx][j] = temp
            candy = bfs(board)
            board[dx][j] = board[i][j]
            board[i][j] = temp

        result = max(result, candy)

        if 0<=dy and dy<n:
            temp = board[i][j]
            board[i][j] = board[i][dy]
            board[i][dy] = temp
            candy = bfs(board)
            board[i][dy] = board[i][j]
            board[i][j] = temp

        result = max(result, candy)
print(result)