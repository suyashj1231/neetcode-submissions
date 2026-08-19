class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxArr = 0
        
        for i in seen:
            if i - 1 not in seen: # begining of sequence
                j = 0
                while i+j in seen:
                    j+=1
                maxArr = max(maxArr, j)

        return maxArr


                

