class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        currset = []
        def backtrack(i):
            if i == len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            backtrack(i+1)
            currset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return subset

