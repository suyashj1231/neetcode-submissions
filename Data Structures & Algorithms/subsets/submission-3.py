class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def backtrack(i, currset):
            if i == len(nums):
                if currset not in subset:
                    subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            backtrack(i+1, currset)
            currset.pop()
            backtrack(i+1, currset)
        
        backtrack(0, [])
        return subset

