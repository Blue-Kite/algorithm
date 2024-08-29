n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
dp = [0 for _ in range(n) for _ in range(n)]

def recur(i, j):
    
    if dp[i][j] != 0:
        return dp[i][j]

    direction=[[0, -1], [0, 1], [-1, 0], [1, 0]]
    
    for k in range(4):
        dx = i + direction[k][0]
        dy = j + direction[k][1]

        if 0 <= dx < n and 0 <= dy < n:
            if nums[i][j] < nums[dx][dy]:
                dp[i][j] =  max(dp[i][j], recur(dx, dy) + 1)
    
    return dp[i][j]

for i in range(n):
    for j in range(n):
        recur(i, j)

print(max(map(max, dp)) + 1)