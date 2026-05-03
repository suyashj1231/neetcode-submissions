class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# kadanes algorithm
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum = max(0, currSum)
            currSum += num
            maxSum = max(currSum, maxSum)

        return maxSum

