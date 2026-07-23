class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # max(nums) and sum(nums)
        left = max(nums)
        right = sum(nums)
        ans = right
        cnt = 1

        while left <= right:
            curr_sum = 0
            mid = left + (right-left)//2

            for val in nums:
                curr_sum += val
                if curr_sum > mid:
                    curr_sum = val
                    cnt +=1
            
            if cnt <=k:
                ans = min(ans,mid)
                right = mid - 1
            else:
                left = mid + 1

            cnt = 1
        
        return ans






        
