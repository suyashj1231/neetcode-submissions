class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            if i+1 > len(nums):
                continue
            l = i+1
            r = len(nums) - 1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    seen.add((nums[i], nums[l], nums[r]))
                    l+=1
                elif total < 0:
                    l +=1
                else:
                    r-=1

        return list(seen)
                
