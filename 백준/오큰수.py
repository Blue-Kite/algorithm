#입력이 100만임 O(N)만에 풀어야함, nlogn이면 100만*20이라 간당간당
import sys
from collections import deque
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
stack = deque([])
answer = [0 for _ in range(n)]

for i in range(n-1, -1, -1):
    while (len(stack) != 0 and stack[0] <= nums[i]):
        stack.popleft()
    if len(stack) == 0:
        answer[i] =  -1
    else:
        answer[i] = stack[0]

    stack.appendleft(nums[i])

print(' '.join(map(str, answer)))
    

