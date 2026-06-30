class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        curr = prices[0]
        while l < len(prices):
            if prices[l] < curr:
                curr = prices[l]
            
            else:
                profit += prices[l] - curr
                curr = prices[l]
            curr 
            l+=1
        return profit

        # for i in range(len(prices)-1):
        #     if prices[i+1] > prices[i]:
        #         profit += prices[i+1] - prices[i]
        
        # return profit