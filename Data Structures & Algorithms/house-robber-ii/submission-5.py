class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i, arr, cache):
        #     if i >= len(arr):
        #         return 0
            
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = max(arr[i] + dfs(i+2,arr, cache), dfs(i+1,arr, cache))

        #     return cache[i]
        # if len(nums)>1:
        #     return(max(dfs(0,nums[1:],{}), dfs(0,nums[0:len(nums)-1],{})))
        # else:
        #     return nums[0]

        def dynamicProg(arr):
            rob1 = 0
            rob2 = 0
            for i in arr:
                temp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
            
        return max(dynamicProg(nums[1:]), dynamicProg(nums[0:-1]),nums[0])
