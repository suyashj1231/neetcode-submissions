class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # [1,3,4,5] , 7
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2 or 1 + dp[1]
        # dp[3] = 1
        # dp[4] = 1
        # dp[5] = 1
        # dp[6] = 1 + dp[5] = 2

        # dp[7] = dp[1] + dp[6] = 1 + 2 = 3, a possible sol
        # dp[7] = dp[3] + dp[4] = 1 + 1 = 2 correct sol
        # dp[7] = dp[4] + dp[3] = 1 + 1 = 2 correct sol
        # dp[7] = dp[2] + dp[5] = 1 + 2 = 3
        def dynamicProg():
            dp = [float('inf')] * (amount+1)
            dp[0] = 0
            #  not btm up so 1 to amt
            for a in range(1, amount+1):
                for c in coins:
                    if a-c >= 0:
                        dp[a] = min(dp[a], 1+dp[a-c])

            return (dp[amount] if dp[amount] != float('inf')
                    else  -1)

        return dynamicProg()
        
        # seen = {}
        # def memoization(i):
        #     if i in seen:
        #         return seen[i]

        #     if i == 0:
        #         return 0
            
        #     if i < 0:
        #         return float('inf')

        #     seen[i] = float('inf')
        #     for c in coins:
        #         seen[i] = min(seen[i], 1 + memoization(i-c))

        #     return seen[i]

        # ans = memoization(amount)
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans

        # def dfs(i):
        #     res = float('inf')
        #     if i == 0:
        #         return 0
            
        #     if i < 0:
        #         return float('inf')

        #     for c in coins:
        #         res =  min(res, 1 + dfs(i-c))

        #     return res

        # ans = dfs(amount)

        # if ans == float('inf'):
        #     return -1

        # else:
        #     return ans 