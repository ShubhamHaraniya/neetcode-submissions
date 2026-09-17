class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        max_sum = 0

        for price in prices:
            mini = min(price,mini)
            max_sum = max(max_sum,price-mini)
        
        return max_sum