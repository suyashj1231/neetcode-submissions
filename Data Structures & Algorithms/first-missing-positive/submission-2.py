class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = len(nums) + 1
        for i in range(1, len(nums)+1):
            if i in nums:
                pass
            else:
                ans = i
                break
        
        return ans