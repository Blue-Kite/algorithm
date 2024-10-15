# 배열 아님 주의

def solution(keyinput, board):
    answer = []
    direction = {'left': [-1, 0] , "right": [1, 0], "up": [0, 1] , "down": [0, -1]}

    width, height = board[0] // 2, board[1] // 2
    x, y= 0, 0
    for d in keyinput:
        dx, dy = direction[d]

        if -width <=x + dx <= width and -height <=y+ dy <= height:
            x = x + dx
            y = y + dy

    answer.append(x)
    answer.append(y)
    return answer