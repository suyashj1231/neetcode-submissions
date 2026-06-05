class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        init = 0
        right = len(nums) - 1
        while init <= right:
            if nums[init] == 0:
                nums[left], nums[init] = nums[init], nums[left]
                left +=1
                init +=1
            
            elif nums[init] == 2:
                nums[right], nums[init] = nums[init], nums[right]
                right -=1
            
            else:
                init +=1
    
                