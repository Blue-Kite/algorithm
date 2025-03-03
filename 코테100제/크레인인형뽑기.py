def solution(board, moves):
    answer = 0
    n = len(board)
    lane = [[] for _ in range(n)]
    stack = [] #바구니 
    
    #역순으로 넣는다
    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[i][j] != 0:
                lane[j].append(board[i][j])
                
    for m in moves:
        if lane[m-1]:
            doll =  lane[m-1].pop()
            if stack and doll == stack[-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(doll)
    return answer