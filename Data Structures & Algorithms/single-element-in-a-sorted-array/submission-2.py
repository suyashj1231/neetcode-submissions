class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r-l) // 2)

            if ((m-1 < 0 or nums[m-1]!= nums[m]) and
            (m+1>=len(nums) or nums[m+1]!= nums[m])):
                return nums[m]

            leftside = m-1 if nums[m-1] == nums[m] else m
            if leftside % 2 == 1: # odd
                r = m - 1
            else: # even
                l = m + 1
