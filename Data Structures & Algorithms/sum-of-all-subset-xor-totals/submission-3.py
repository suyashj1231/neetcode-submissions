class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        currset = []
        subset = []
        def backtrack(i, currset):
            if i == len(nums):
                subset.append(currset.copy())
                return subset

            currset.append(nums[i])
            backtrack(i+1, currset)

            currset.pop()
            backtrack(i+1, currset)
            
        backtrack(0, currset)
        for sub in subset:
            current = 0
            for i in sub:
                current ^= i

            total+= current
        return total