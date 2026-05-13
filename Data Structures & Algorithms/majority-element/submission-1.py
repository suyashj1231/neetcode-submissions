class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currmax = float('-inf')
        count = 0
        for i in range(len(nums)):
            if nums[i] == currmax:
                count += 1
            
            elif count <= 0:
                currmax = nums[i]
                count = 1
                
            else:
                count -=1
        
        return currmax
            
            
