class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [i * -1 for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap)
            b = heapq.heappop(maxHeap)
            if b > a:
                heapq.heappush(maxHeap, a-b)

        maxHeap.append(0)
        return abs(maxHeap[0])            