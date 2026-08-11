class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSeen = float('-inf')
        runningSum = 0

        for i in nums:
            runningSum += i
            if runningSum > maxSeen:
                maxSeen = runningSum

            if runningSum < 0:
                runningSum = 0
        
        return maxSeen
        