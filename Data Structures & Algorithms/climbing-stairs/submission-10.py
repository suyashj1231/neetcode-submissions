class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp1 = 1
        dp2 = 2

        for i in range(3,n+1):
            new = dp1 + dp2
            dp1 = dp2
            dp2 = new
        return new


        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # dp = [0] * (n+1) 
        # dp[1] = 1 # ways to reach step 1 is 1 and
        # dp[2] = 2 # ways to reach step 2 is 22...
        
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]


        # seen = {}
        # def memoization(i):
        #     if i in seen:
        #         return seen[i]
        #     if i == n:
        #         return 1
        #     elif i>n:
        #         return 0
        #     seen[i] =  memoization(i+1) + memoization(i+2)
        #     return seen[i]
        # return memoization(0)


        # ways = []
        # def dfs(i):
        #     if i == n:
        #         ways.append(1)
        #         return

        #     if i>n:
        #         return

        #     dfs(i+1)
        #     dfs(i+2)

        # dfs(0)
        # return sum(ways)
