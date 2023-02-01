from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in permutations(nums, n):
  sum = 0
  for j in range(0, n-1):
    sum += abs(i[j]-i[j+1])
  if ans < sum:
    ans = sum
print(ans)