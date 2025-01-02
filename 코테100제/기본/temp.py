N, K = map(int, input().split())
bag = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    bag.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v = bag[i][1]

        if j - w < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])


return dp[n][k]