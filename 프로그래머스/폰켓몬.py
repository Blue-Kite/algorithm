def solution(nums):
    answer = 0
    k = len(nums) // 2
    return min(k, len(set(nums)))