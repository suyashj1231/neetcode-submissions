class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0
        def backtrack(i, currset):
            if i == len(nums):
                res = 0
                for num in currset: res ^= num
                self.total += res
                return

            currset.append(nums[i])
            backtrack(i+1, currset)

            currset.pop()
            backtrack(i+1, currset)

        backtrack(0, [])
        return self.total