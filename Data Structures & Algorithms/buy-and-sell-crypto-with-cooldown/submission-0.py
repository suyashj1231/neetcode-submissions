class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dp = {}
        # state : buying = true, selling = false
        # if i am buying: then then would be i + 1
        # if i am selling then next would be i+ 2 coz i+1 would be cooldown

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            

            if buying: # so we buy a stock
                buy = dfs(i+1, not buying) - prices[i]
                cooldwn =  dfs(i+1, buying) 
                dp[(i, buying)] = max(buy, cooldwn)
            
            else: # selling
                sell = dfs(i+2, not buying) + prices[i]
                cooldwn =  dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldwn)
            
            return dp[(i, buying)]
        
        return dfs(0, True)