class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < target:
                    ans+= r-l
                    l+=1
                else:
                    r-=1
        return ans