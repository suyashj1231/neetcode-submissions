class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        curr = []
        def helper(i, curr):
            if i >= len(nums):
                subset.append(curr.copy())
                return

            curr.append(nums[i])
            helper(i+1,curr)

            curr.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1,curr)
        
        helper(0, curr)
        return subset