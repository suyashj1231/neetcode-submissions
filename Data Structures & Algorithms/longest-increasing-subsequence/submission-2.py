class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1+ LIS[j])
        
        return max(LIS)


        # curr = 0
        # seen = {}
        # def memoization(i):
        #     if i == len(nums) - 1:
        #         return 1

        #     if i in seen:
        #         return seen[i]

        #     seen[i] = 1
        #     for j in range(i+1, len(nums)):
                
        #         if nums[j] <= nums[i]:
        #             continue

        #         seen[i] = max(seen[i], 1 + memoization(j))

        #     return seen[i]

        # for i in range(len(nums)):
        #     curr = max (curr, memoization(i))
        
        # return curr
        
        # curr = 0
        # def backtrack(i):
        #     if i == len(nums)-1:
        #         return 1

        #     maxseen = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[j] <= nums[i]:
        #             continue
        #         maxseen = max(maxseen, 1 + backtrack(j))

        #     return maxseen

        # for i in range(len(nums)):
        #     curr = max (curr, backtrack(i))
        
        # return curr