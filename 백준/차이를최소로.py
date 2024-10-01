#https://www.acmicpc.net/problem/3090
'''
차이의 최댓값이 x번일 때 연산 횟수를 구함
x<=t x를 더 작게, 목표에 해당하니 욕심을 내서
t>t  x를 더 크게
'''

n, t = map(int, input().split())
nums = list(map(int, input().split()))
s = 0
e = max(nums)
result = e

def cal(nums, x):
    cnt = 0#연산횟수
    #왼 -> 오
    nums2 = [i for i in nums]
    
    for i in range(0, n-1, 1):
        if nums2[i+1] > nums2[i] + x:
            cnt += nums2[i+1] - (nums2[i] + x)
            nums2[i+1] = nums2[i] + x

    #오 -> 왼
    for j in range(n-1, 0, -1):
        if nums2[j] + x < nums2[j-1]:
            cnt += nums2[j-1] - (nums2[j] + x)
            nums2[j-1] = nums2[j] + x

    return cnt

while s<=e:
    x = (s+e) // 2 #차이의 최대값
    cnt = 0
    cnt = cal(nums, x)
    if cnt <= t:
        e = x - 1
        result = min(result, x)
    else:
        s = x + 1

for i in range(0, n-1, 1):
    if nums[i+1] > nums[i] + result:
        nums[i+1] = nums[i] + result

#오 -> 왼
for j in range(n-1, 0, -1):
    if nums[j] + x < nums[j-1]:
        nums[j-1] = nums[j] + result

print(*nums)