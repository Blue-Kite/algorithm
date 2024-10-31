def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]

    #현재 위치에서 갈 수 있는 곳 : 바로 아래, 오른쪽 대각선 
    for i in range(0, n-1):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

    return max(dp[n-1])