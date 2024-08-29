n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

result = 0
s = 0
e = len(nums) - 1

while s < e:
    sumN= nums[s] + nums[e] 
    if sumN == x:
        e -= 1
        result += 1

    elif sumN > x:
        e -= 1
    else:
        s += 1

print(result)