#무게는 1부터 가치는 0부터 
#dp[N][K] 배열
#각각 i, j 인덱스면 i번째 물건까지 포함하고 j 무게만큼 담을때 최대가치 
#물건을 담지 않는경우 , 지금 물건의 무게만큼 여유가 있어서 물건을 담은경우

import sys
n, k = map(int, sys.stdin.readline().split())
bags = []
for _ in range(n):
    bags.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]


for i in range(1, n+1):
    bag = bags[i-1]
    for j in range(0, k+1):
        dp[i][j] = dp[i-1][j] #j무게만큼 담았는데 해당물건은 담지 않는경우 
        if bag[0] <= j: #j무게보다 작으면, 모든 j에 대해서 테스트 
            dp[i][j] = max(dp[i][j], bag[1] + dp[i-1][j - bag[0]])
print(dp[n][k])