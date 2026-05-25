class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redP = 0
        blueP = len(nums) - 1
        current = 0

        while current <= blueP:
            if nums[current] == 0:
                nums[current], nums[redP] = nums[redP], nums[current]
                current += 1
                redP += 1

            elif nums[current] == 2:
                nums[current], nums[blueP] = nums[blueP], nums[current]
                blueP -=1

            else:
                current +=1



            