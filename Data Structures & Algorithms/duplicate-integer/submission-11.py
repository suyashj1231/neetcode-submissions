class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
#s1
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.add(i)
        # return False
#s2
        # while nums:
        #     first = nums.pop()
        #     if first in nums:
        #         return True
        # return False

#s3
        seen = set(nums)
        return len(seen) != len(nums)