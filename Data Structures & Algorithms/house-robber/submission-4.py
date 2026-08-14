class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i):, Sequence
        #     if i >=len(nums):
        #         return 0
                
        #     return max(nums[i]+dfs(i+2), dfs(i+1))
        
        # return dfs(0)
    
        seen = {}
        def memo(i):
            if i in seen:
                return seen[i]
            
            if i >=len(nums):
                return 0
            
            seen[i] = max(nums[i]+memo(i+2), memo(i+1))

            return seen[i]

        return memo(0)
        
            