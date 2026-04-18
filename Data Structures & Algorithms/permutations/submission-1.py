class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]
            
            res = []
            perms = helper(i+1)
            for p in perms:
                for j in range(len(p)+1):
                    cop = p.copy()
                    cop.insert(j, nums[i])
                    res.append(cop)
            
            return res
        
    
        return helper(0)

        
        