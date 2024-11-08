N, K = map(int, input().split())
bag = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    bag.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v = bag[i][]


return dp[n][k]