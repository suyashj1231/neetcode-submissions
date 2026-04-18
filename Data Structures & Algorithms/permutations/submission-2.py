class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]
            
            res = []
            perms = helper(i+1)
            for p in perms:
                for j in range(len(p)+1):
                    p_cop = p.copy()
                    p_cop.insert(j,nums[i])
                    res.append(p_cop)
            return res

        return helper(0)

