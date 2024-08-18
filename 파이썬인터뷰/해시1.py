class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for c in list(stones):
            if c in jewels:
                answer += 1

        return answer

# sum([s in jewels for s in stones])