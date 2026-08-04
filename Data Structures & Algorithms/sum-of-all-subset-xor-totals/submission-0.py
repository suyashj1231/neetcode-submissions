class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        currset = []
        subset = []
        ans = 0
        def backtrack(currset, i):
            if i == len(nums):
                subset.append(currset.copy())
                return

            currset.append(nums[i])
            backtrack(currset, i+1)
            currset.pop()
            backtrack(currset, i+1)
        
        backtrack([],0)
        for sub in subset:
            res = 0
            for num in sub:
                res ^= num
            ans += res
        return ans

