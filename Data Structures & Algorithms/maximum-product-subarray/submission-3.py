class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 1
        minProd = 1
        ans = nums[0]

        for n in range(len(nums)):
            if nums[n] < 0:
                minProd, maxProd = maxProd, minProd
            
            minProd = min(nums[n], minProd * nums[n])
            maxProd = max(nums[n], maxProd * nums[n])
            ans = max(ans, maxProd)
        
        return ans
            
            