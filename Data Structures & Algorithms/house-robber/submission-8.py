class Solution:
    def rob(self, nums: List[int]) -> int:
        # # O(n) - space and O(n) - time

        # if len(nums) == 1: return nums[0]
        # dp = [0]* (len(nums))
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])
        # for i in range(2,len(nums)):
        #     dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        # return dp[-1]

        # O(1) - space and O(n) - time
        if len(nums) == 1: return nums[0]
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            new = max(rob1+ nums[i], rob2)
            rob1 = rob2
            rob2 = new
        
        return rob2



