class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(0,n-3):
            for j in range(i+1, n-2):
                l = j + 1
                r = n - 1
                while l < r:
                    current = nums[i] + nums[j] + nums[l] + nums[r]
                    if current > target:
                        r-=1
                    elif current < target:
                        l+=1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l+=1
                        r-=1
        return list(res)
                
            