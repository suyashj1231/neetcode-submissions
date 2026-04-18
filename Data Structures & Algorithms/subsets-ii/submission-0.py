class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        sub = []
        nums.sort()
        self.helper(0, nums, curr, sub)
        return sub

    def helper(self,i, nums, currset, subset):
        if i >= len(nums):
            subset.append(currset.copy())
            return
        currset.append(nums[i])
        self.helper(i+1, nums, currset, subset)
        
        currset.pop()
        while i+1  < len(nums) and nums[i] == nums[i+1]:
            i +=1
        self.helper(i+1, nums, currset, subset)