def solution(dirs):
    answer = 0
    board = [[0 for _ in range(10)] for _ in range(10)]
    x, y = 5, 5
    board[5][5] = 1
    
    for d in list(dirs):
        if d == 'U':
            nx, ny = x, y - 1
        elif d == 'D':
            nx, ny = x, y + 1
        elif d == 'R':
            nx, ny = x+1, y
        else:
            nx, ny = x-1, y
            
        if 0<= nx < 10 and 0<=ny < 10:
            x, y = nx, ny
            if board[y][x] == 0:
                board[y][x] = 1
                answer += 1 
    return answer