# 692. Top K Frequent Words https://leetcode.com/problems/top-k-frequent-words/
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for w in counter:
            heapq.heappush(heap, (-counter[w], w)) # 빈도수의 내림차순, 원래값 오름차순
        
        answer = []
        for _ in range(k):
            cnt, n = heapq.heappop(heap)
            answer.append(n)
        return answer
