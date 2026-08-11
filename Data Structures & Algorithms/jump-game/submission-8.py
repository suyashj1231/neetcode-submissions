from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = {}
        def memoization(i):
            if i in seen:
                return seen[i]
            
            if i == len(nums) - 1:
                return True
            
            if i >= len(nums):
                return False

    
            for j in range(1,nums[i]+1):
                run = memoization(i+j)
                if run:
                    seen[i] = run
                    return True

            seen[i] = False
            return False

        return memoization(0)

                

            
        # def dfs(i):
        #     if i == len(nums) - 1:
        #         return True

        #     if i >= len(nums):
        #         return False

        #     for j in range(1,nums[i]+1):
        #         if dfs(i+j):
        #             return True
            
        #     return False
        
        # return dfs(0)


        # def bfs():
        #     queue = deque()
        #     queue.append(0)
        #     visited = set()
        #     visited.add(0)
        #     while queue:
        #         curr = queue.popleft()
        #         if curr == len(nums) - 1:
        #             return True

        #         for i in range(1, nums[curr]+1): # 0 means same i guess we can inc. but uesless
        #             newIdx = i + curr
        #             if (newIdx not in visited and
        #                 newIdx < len(nums)):
        #                 queue.append(newIdx)
        #                 visited.add(newIdx)
        #     return False
        
        # return bfs()
                
                
                

                

        