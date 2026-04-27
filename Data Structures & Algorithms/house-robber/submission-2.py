class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dynamicProg():
            rob1, rob2 =0, 0
            # rob1, rob2, m, n+1 .. 
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return dynamicProg()
               
        
        # cache = {}
        # def memoization(i, cache):
        #     if i in cache:
        #         return cache[i]

        #     if i >= len(nums):
        #         return 0
            
        #     cache[i] = max((nums[i]+memoization(i+2, cache)), memoization(i+1, cache))
        #     return cache[i]

        # return memoization(0, cache)

        
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
            
        #     return max(nums[i]+dfs(i+2), dfs(i+1))
        
        # return dfs(0)