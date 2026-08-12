class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = [i for i in range(1, len(nums)+1)]
        for i in set(nums):
            ans.remove(i)
        return ans           
