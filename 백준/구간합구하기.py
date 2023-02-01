import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
indexpair = []
for _ in range(m):
    indexpair.append(list(map(int, sys.stdin.readline().split())))

prexsum = []
prexsum.append(nums[0])
for i in range(1, n):
    n = prexsum[i-1]+nums[i] 
    prexsum.append(n)

for i in range(m):
    k, j = indexpair[i][0], indexpair[i][1]
    if k == 1:
        print(prexsum[j-1])
    else:
        print(prexsum[j-1] - prexsum[k-2])

