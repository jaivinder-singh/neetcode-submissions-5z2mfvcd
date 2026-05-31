class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        for i in range(len(prices) - 1):
            if prices[i+ 1] > prices[i]:
                profit = prices[i+1] - prices[i]
                maxProfit += profit

        return maxProfit
            
        