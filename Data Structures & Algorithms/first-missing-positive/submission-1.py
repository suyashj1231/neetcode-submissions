class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            if i in nums:
                pass
            else:
                return i
        
        return len(nums) + 1