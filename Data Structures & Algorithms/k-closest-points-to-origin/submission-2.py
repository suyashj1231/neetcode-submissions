class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # store in heap -> distance from origin and value
        # we need to use min heap with max size of k
        heap = []
        for x,y in points:
            distance = ((0-x)**2 + (0-y)**2)**0.5
            heap.append([distance, x, y])
        heapq.heapify(heap)
        
        ans = []
        for i in range(k):
            val = heapq.heappop(heap)
            x = val[1]
            y = val[2]
            ans.append([x,y])

        return ans
