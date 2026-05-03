from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def bfs():
            queue = deque()
            queue.append(0)
            visited = set([0])

            while queue:
                curr = queue.popleft()
                if curr == len(nums) - 1:
                    return True
                
                start = curr + 1
                end = nums[curr] + curr + 1
                for j in range(start, end):
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
            
            return False
        
        return bfs()


        # visited = {}
        # def memoization(i):
        #     if i == len(nums)-1:
        #         return True
            
        #     if i in visited:
        #         return visited[i]

        #     start = i+1
        #     end = i + nums[i] + 1

        #     for j in range(start, end):
        #         run = memoization(j)
        #         if run:
        #             visited[i] = run
        #             return True
        #     visited[i] = False
        #     return False

        # return memoization(0)
        
        
        
        
        
        # def dfs(i):
        #     if i == len(nums)-1:
        #         return True
            
        #     start = i+1
        #     end = i + nums[i] + 1

        #     for j in range(start, end):
        #         if dfs(j):
        #             return True
        #     return False

        # return dfs(0)