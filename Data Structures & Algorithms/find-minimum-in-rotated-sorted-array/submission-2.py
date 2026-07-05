class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l< r:
            mid = l + (r-l) // 2

            if nums[mid] < nums[r]: # sorted from mid to R, i.e smol to big
                r = mid
            else: # nums[mid] > nums[l] from l to mid is sorted and min val must be in here
                l = mid + 1

        return nums[l]
        