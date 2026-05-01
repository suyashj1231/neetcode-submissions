# we can take a double digit val only when 1st digit starts with 1 , then 2nd digit
# can be b/w (0-9) as 10 - 19 < 26
# start with 2 , then 2nd digit has to be b/w 0 to 6
# start with 3,4,5 ... then no 2nd digit
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1] # same as dfs(i+1)
            if i + 1 < len(s) and 9 < int(s[i:i+2]) < 27:
                dp[i] += dp[i+2]
        return dp[0]
           
        # seen = {}
        # def memoization(i):
        #     if i == len(s):
        #         return 1

        #     if i in seen:
        #         return seen[i]
            
        #     if s[i] == '0':
        #         return 0
            
        #     seen[i] = memoization(i+1)
        #     if i + 1 < len(s) and 9 < int(s[i:i+2]) < 27:
        #         seen[i] = seen[i] + memoization(i+2)

        #     return seen[i]
        
        # return memoization(0)


        # def dfs(i):
        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
        #     res = dfs(i+1)

        #     if i + 1 < len(s) and 9 < int(s[i:i+2]) < 27:
        #         res = res + dfs(i+2)
        #     return res
        # return dfs(0)

