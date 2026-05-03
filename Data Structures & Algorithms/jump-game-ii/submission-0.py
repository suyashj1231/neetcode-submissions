class Solution:
    def jump(self, nums: List[int]) -> int:
        def bfs():
            queue = deque()
            queue.append(0)
            visited = set([0])
            path = 0
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr == len(nums) - 1:
                        return path
                    start = curr + 1
                    end = nums[curr] + curr + 1
                    for j in range(start, end):
                        if j not in visited:
                            visited.add(j)
                            queue.append(j)
                path += 1
            return -1
        return bfs()