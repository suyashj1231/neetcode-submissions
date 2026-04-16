class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_list = []
        for i in range(len(nums)):
            left = nums[0:i] if i > 0 else [1]
            right = nums[i+1:]
            product = 1
            for i in left:
                product = product * i
            
            for j in right:
                product = product * j
            ans_list.append(product)
    
        return ans_list

