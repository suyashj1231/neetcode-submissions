class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        l = 0
        while l < len(nums):
            req = target - nums[l]
            if req in seen:
                return [seen[req], l]
            seen[nums[l]] = l
            l+=1

        