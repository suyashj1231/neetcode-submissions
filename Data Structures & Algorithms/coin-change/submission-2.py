class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {}
        def memoization(i):
            if i in seen:
                return seen[i]

            if i == 0:
                return 0
            
            if i < 0:
                return float('inf')

            seen[i] = float('inf')
            for c in coins:
                seen[i] = min(seen[i], 1 + memoization(i-c))

            return seen[i]

        ans = memoization(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans

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