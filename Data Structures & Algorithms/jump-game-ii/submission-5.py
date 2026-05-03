class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy bfs
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i + nums[i])
            
            l = r + 1
            r = far
            res +=1
        return res


        # ** UPGRADED VERSION **
        # def bfs():
        #     queue = deque([0])
        #     path = 0
        #     max_enqueued = 0
        #     while queue:
        #         for _ in range(len(queue)):
        #             curr = queue.popleft()
        #             if curr == len(nums) - 1:
        #                 return path
                    
        #             start = curr + 1
        #             start = max(start, max_enqueued + 1)
        #             end = nums[curr] + curr + 1
        #             for j in range(start, end):
        #                 queue.append(j)
        #                 max_enqueued = j
        #         path += 1
        #     return -1
        # return bfs()

        # bfs original 
        # def bfs():
        #     queue = deque()
        #     queue.append(0)
        #     visited = set([0])
        #     path = 0
        #     while queue:
        #         for _ in range(len(queue)):
        #             curr = queue.popleft()
        #             if curr == len(nums) - 1:
        #                 return path
        #             start = curr + 1
        #             end = nums[curr] + curr + 1
        #             for j in range(start, end):
        #                 if j not in visited:
        #                     visited.add(j)
        #                     queue.append(j)
        #         path += 1
        #     return -1
        # return bfs()