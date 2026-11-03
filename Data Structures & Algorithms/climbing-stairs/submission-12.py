class Solution:
    def climbStairs(self, n: int) -> int:
        self.ans = 0
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if i > n:
                return 0

            memo[i] = dfs(i+1) + dfs(i+2)
            
            return memo[i]
    
       
        return dfs(0)