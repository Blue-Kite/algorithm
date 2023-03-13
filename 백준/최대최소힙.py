import heapq
import sys

"""
최소힙
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if len(nums) == 0 and n == 0:
        print(0)
    
    if len(nums) != 0 and n == 0:
        print(heapq.heappop(nums))
    
    if n != 0:
        heapq.heappush(nums, n)
"""
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if len(nums) == 0 and n == 0:
        print(0)
    
    if len(nums) != 0 and n == 0:
        print(-heapq.heappop(nums))
    
    if n != 0:
        heapq.heappush(nums, -n)

