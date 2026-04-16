class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.add(i)
        # return False

        while nums:
            first = nums.pop()
            if first in nums:
                return True
        return False