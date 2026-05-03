class Solution:
    def jump(self, nums: List[int]) -> int:
        def bfs():
            queue = deque([0])
            path = 0
            max_enqueued = 0
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr == len(nums) - 1:
                        return path
                    
                    start = curr + 1
                    start = max(start, max_enqueued + 1)
                    end = nums[curr] + curr + 1
                    for j in range(start, end):
                        queue.append(j)
                        max_enqueued = j
                path += 1
            return -1
        return bfs()