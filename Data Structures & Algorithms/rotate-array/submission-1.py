class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = (len(nums) - k % len(nums)) % len(nums)

        for _ in range(k):
            l = 1
            while l < len(nums)-1:
                nums[l+1],nums[l] = nums[l],nums[l+1]
                l+=1
            nums[0], nums[-1] = nums[-1], nums[0]
