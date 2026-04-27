class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, arr, cache):
            if i >= len(arr):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(arr[i] + dfs(i+2,arr, cache), dfs(i+1,arr, cache))

            return cache[i]
        if len(nums)>1:
            return(max(dfs(0,nums[1:],{}), dfs(0,nums[0:len(nums)-1],{})))
        else:
            return nums[0]