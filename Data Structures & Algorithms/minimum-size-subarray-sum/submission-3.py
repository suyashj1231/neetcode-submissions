class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        currSum = 0
        ans = float('inf')
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >=target: # we reduce from L
                ans = min(ans, r-l+1)
                currSum -= nums[l]
                l+=1

        if ans == float('inf'):
            return 0

        return ans

