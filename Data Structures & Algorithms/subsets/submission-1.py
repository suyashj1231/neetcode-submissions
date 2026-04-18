class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currset = []
        sub = []
        def helper(i, subset):
            if i >= len(nums):
                subset.append(currset.copy())
                return
            currset.append(nums[i])
            helper(i+1, subset)
            
            currset.pop()
            helper(i+1, subset)
        
        helper(0, sub)
        return sub