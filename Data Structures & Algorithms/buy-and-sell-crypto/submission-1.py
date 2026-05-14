class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            minPrice = min(minPrice, price)

            profit = price - minPrice

            maxProfit = max(profit, maxProfit)
        
        return maxProfit

