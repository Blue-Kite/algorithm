import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
answer = 0
for i in range(1, n-1):
    mid = nums[i]
    answer = max(answer, abs(nums[i-1]+nums[n-1]+nums[i] - nums[i]*3))
    answer = max(answer, abs(nums[0]+nums[i+1]+nums[i]- nums[i]*3))
print(answer)