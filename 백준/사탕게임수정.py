#220501
#백준 3085번 사탕게임 
#https://www.acmicpc.net/problem/3085

def count(board): #배열에서 최대 사탕인지 확인 
    row, col, row_max, col_max = 1, 1, -1e9, -1e9
    n = len(board)
    for i in range(n): #같은 행 다른 열 (0~n-1)
        for j in range(n-1): #0 ~n-2
            if board[i][j] == board[i][j+1]:
                row += 1
            else:
                row = 1
            row_max = max(row, row_max) #해당 행에서 연속적인 색깔 영역중 큰거 
        row = 1 #다음행을 위해 초기화

    for j in range(n): # 다른 행 같은 열, 아래로 내려가면서 비교 
        for i in range(n-1):    
            if board[i][j] == board[i+1][j]: 
                col += 1
            else:
                col = 1
            col_max = max(col_max, col)
        col = 1
    answer = max(row_max, col_max)
    return answer

n = int(input())
board = []
#for i in range(n): # 파이썬 팁: list(문자열) -> [한글자씩]
#   board.append(list(input()))
board = [list(input()) for _ in range(n)]
result = 0

de = [[-1, 0], [1, 0], [0,-1], [0, 1]] #상하좌우

for i in range(n):
    for j in range(n): #모든 좌표 

        for k in range(4): #4가지 방향
            nx = i + de[k][0] 
            ny = j + de[k][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n: #범위 안이면 
                continue
            if board[i][j] != board[nx][ny]:           #다른 사탕이라면 
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j] #교환해보고 
                result = max(result, count(board))                      #최대크기 사탕이라면
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j] #최대 크기아니라면 원위치 
                
print(board)