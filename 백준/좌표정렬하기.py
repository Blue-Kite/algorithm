import sys
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))
nums.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(nums[i][0], nums[i][1])