class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        curr = float('inf')

        while l < len(prices):
            if prices[l] < curr:
                curr = prices[l]
            
            else:
                profit = max(profit, prices[l] - curr)

            l+=1
        return profit