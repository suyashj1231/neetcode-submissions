class Solution:
    def climbStairs(self, n: int) -> int:
        curr = {}
        def memoization(num, curr):
            if num < 2:
                return 1
            if num in curr:
                return curr[num]
            
            curr[num] = memoization(num-1, curr) + memoization(num-2, curr)
            return curr[num]
        
        return memoization(n, curr)