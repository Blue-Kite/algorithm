class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = {}
        for idx, item in enumerate(nums):
            if target-item in search:
                return [search[target-item], idx]
            else:
                search[item] = idx