class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        res = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(maxHeap, [dist, [x, y]])
        
        while k>0:
            res.append(heapq.heappop(maxHeap)[1])
            k = k-1
        
        return res

