class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minprice = sys.maxsize

        for price in prices:
            minprice = min(minprice, price)
            answer = max(answer, price-minprice)
        
        return answer 