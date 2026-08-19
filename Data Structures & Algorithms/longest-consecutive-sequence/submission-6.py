class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxArr = 0
        
        for i in (seen):
            if i - 1 not in seen: # begining of sequence
                cnt = 1
                j = i+1
                while j in seen:
                    cnt+=1
                    j+=1
                maxArr = max(maxArr, cnt)

        return maxArr


                

