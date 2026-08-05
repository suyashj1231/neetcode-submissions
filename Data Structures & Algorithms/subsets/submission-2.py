class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currset = []
        subset = []
        end = len(nums)
        def backtrack(currset, i):
            if i == end:
                subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            backtrack(currset,i+1)

            currset.pop()
            backtrack(currset,i+1)
        
        backtrack(currset,0)
        return subset

        