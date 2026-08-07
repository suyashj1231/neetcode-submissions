class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_max = 0
        max_freq = 0
        for i in nums:
            if i == curr_max:
                max_freq +=1
            elif max_freq <= 0:
                curr_max = i
                max_freq = 1
            else:
                max_freq -=1
        
        return curr_max