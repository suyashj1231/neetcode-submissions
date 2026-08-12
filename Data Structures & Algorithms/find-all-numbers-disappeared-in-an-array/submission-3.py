class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            i = abs(i)
            nums[i-1] = -1 * abs(nums[i-1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
           
        