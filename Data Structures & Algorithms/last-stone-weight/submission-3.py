class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [i * -1 for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            a = heapq.heappop(maxHeap) * -1
            b = heapq.heappop(maxHeap) * -1
            print(a,b)
            if a == b:
                pass
            
            elif a > b:
                heapq.heappush(maxHeap, (a-b)*-1)
            
            else:
                heapq.heappush(maxHeap, (b-a)*-1)

        if len(maxHeap) == 1:
            return maxHeap[0] * -1
        
        else:
            return 0


            