class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = 1
        answer = []

        for i in range(len(nums)):
            answer.append(n)
            n = n * nums[i]
        
        n = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * n
            n = n * nums[i]
        return answer