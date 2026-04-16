class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        sub = []
        self.helper(0, nums, curr, sub)
        return sub

    def helper(self,i, nums, currset, subset):
        if i >= len(nums):
            subset.append(currset.copy())
            return
        currset.append(nums[i])
        self.helper(i+1, nums, currset, subset)
        currset.pop()

        self.helper(i+1, nums, currset, subset)