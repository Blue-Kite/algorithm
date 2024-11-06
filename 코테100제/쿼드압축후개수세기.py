#0의 개수, 1의 개수 
def calc(board):
    s = sum(sum(row) for row in board)
    if s == 0:
        return 1, 0
    if s == len(board) ** 2:
        return 0, 1

    #만약 1도, 0도 아니라면 쪼개야함 
    n = len(board) // 2 #반으로 쪼개기
    num0, num1 = 0, 0

    a, b = calc([row[:n] for row in board[:n]])
    num0 += a
    num1 += b

    a, b = calc([row[n:] for row in board[:n]])
    num0 += a
    num1 += b

    a, b = calc([row[:n] for row in board[n:]])
    num0 += a
    num1 += b

    a, b = calc([row[n:] for row in board[n:]])
    num0 += a
    num1 += b

    return num0, num1

def solution(arr):
    return calc(arr)