from itertools import combinations
n,s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    for j in list(combinations(nums, i)):
        if sum(j) == s:
            ans += 1
print(ans)