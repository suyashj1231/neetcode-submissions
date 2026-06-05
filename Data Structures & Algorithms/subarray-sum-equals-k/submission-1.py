class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        currSum = 0
        total = 0
        for i in range(len(nums)):
            currSum = currSum + nums[i]

            preVal = currSum - k

            if preVal in prefixSum:
                total += prefixSum[preVal]

            prefixSum[currSum] = prefixSum.get(currSum,0) + 1
        
        return total
        



    



