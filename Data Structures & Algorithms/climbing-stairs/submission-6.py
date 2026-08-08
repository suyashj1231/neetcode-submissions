class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {}
        def memoization(i):
            if i in seen:
                return seen[i]
            if i == n:
                return 1
            elif i>n:
                return 0

            seen[i] =  memoization(i+1) + memoization(i+2)

            return seen[i]

        return memoization(0)


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
