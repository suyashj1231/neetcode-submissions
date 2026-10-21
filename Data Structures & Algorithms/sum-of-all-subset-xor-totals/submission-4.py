class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        def backtrack(i, currset):
            if i == len(nums):
                result = 0
                for num in currset: result ^= num
                subset.append(result)
                return

            currset.append(nums[i])
            backtrack(i+1, currset)

            currset.pop()
            backtrack(i+1, currset)

        backtrack(0, [])
        print(subset)
        return sum(subset)