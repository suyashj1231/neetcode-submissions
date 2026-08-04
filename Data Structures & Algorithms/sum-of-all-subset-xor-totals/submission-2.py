class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        currset = []
        self.total = 0
        def backtrack(currset, i):
            if i == len(nums):
                res = 0
                for num in currset:
                    res ^= num
                self.total += res
                return

            currset.append(nums[i])
            backtrack(currset, i+1)
            currset.pop()
            backtrack(currset, i+1)
        
        backtrack([],0)
        return self.total

