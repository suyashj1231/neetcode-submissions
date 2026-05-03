class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = 1
        maxMul = nums[0]

        for n in range(len(nums)):
            if nums[n] < 0:
                temp = currMax
                currMax = currMin
                currMin = temp

            currMax = max(nums[n], currMax * nums[n])
            currMin = min(nums[n], currMin * nums[n])

            if currMax > maxMul:
                maxMul = currMax
        return maxMul

