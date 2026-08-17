class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l = j+1
                r = len(nums)-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total == target:
                        seen.add((nums[i], nums[j], nums[l], nums[r]))
                        l+=1
                        r-=1
                    elif total < target:
                        l+=1
                    else:
                        r-=1
        
        return list(seen)

