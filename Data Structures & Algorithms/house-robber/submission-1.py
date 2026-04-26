class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def memoization(i, cache):
            if i in cache:
                return cache[i]

            if i >= len(nums):
                return 0
            
            cache[i] = max((nums[i]+memoization(i+2, cache)), memoization(i+1, cache))
            return cache[i]
        return memoization(0, cache)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     return max(nums[i]+dfs(i+2), dfs(i+1))
        
        # return dfs(0)