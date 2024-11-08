import sys
input = sys.stdin.readline

#백준 평범한 배낭
#냅색문제 
N, K = map(int, input().split())
bag = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    bag.append(list(map(int, input().split())))

#dp : i번째 물건, j 가방 무게 일때 물건들의 가치합
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = bag[i][0] 
        v = bag[i][1]
       
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
print(dp[N][K])