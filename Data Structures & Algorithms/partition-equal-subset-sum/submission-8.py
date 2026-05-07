class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) / 2

        visited = {} # index, target - val

        def memo(i, remaining):
            if remaining == 0:
                return True
        
            if i == len(nums) or remaining < 0:
                return False
            
            if (i, remaining) in visited:
                return visited[(i, remaining)]


            visited[(i, remaining)] = (memo(i+1, remaining - nums[i]) or
                                       memo(i+1, remaining))

            return visited[(i, remaining)]

        for i in range(len(nums)):
            if memo(i, target):
                return True
        
        return False
        