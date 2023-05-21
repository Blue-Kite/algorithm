#모든 칸의 수는 100만이라서 한번 훝을때 바로 계산가능해야함
#해당칸이 맨 오른쪽 아래칸인 경우 가장 큰 정사각형의 크기
#왼쪽위, 위, 왼쪽의 dp 배열에서 가장 작은 값과 자기자신을 더하면 됨
#사이드는 초기값 설정 
#특이사항 : [[1,0],[0,0]] => 1

def solution(board):
    answer = 0 
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    #초기값설정
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0:
                dp[i][j] = board[i][j]
            if j == 0:
                dp[i][j] = board[i][j] 굳이..? """
    dp = board.copy()

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            #일단 해당칸부터 1일때 
            if board[i][j] == 1:
                cnt = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) 
                dp[i][j] = cnt + 1
            
    answer = max(map(max, dp))
    #print(answer*answer)
    return answer*answer
    