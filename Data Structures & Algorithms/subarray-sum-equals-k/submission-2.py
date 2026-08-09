class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = {0:1}
        currsum = 0

        for i in nums:
            currsum += i
            diff = currsum - k
            total += prefix.get(diff,0)

            prefix[currsum] = prefix.get(currsum, 0) + 1
        return total


        