from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def bfs():
            queue = deque()
            queue.append(0)
            visited = set()
            visited.add(0)
            while queue:
                curr = queue.popleft()
                if curr == len(nums) - 1:
                    return True

                for i in range(1, nums[curr]+1): # 0 means same i guess we can inc. but uesless
                    newIdx = i + curr
                    if (newIdx not in visited and
                        newIdx < len(nums)):
                        queue.append(newIdx)
                        visited.add(newIdx)
            return False
        
        return bfs()
                
                
                

                

        