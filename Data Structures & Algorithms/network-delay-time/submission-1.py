class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # initial src is k
        # times = src, dst, w
        # min weight that reach cities - Djistra's

        # lets make a adj list and then a minHeap

        adj = {}
        shortest = {}
        for i in range(1, n+1):
            adj[i] = []
            shortest[i] = -1
        
        for src, dst, wt in times:
            adj[src].append((wt, dst))

        # ad starting pt
        minHeap = [(0,k)]
        total_network = 0
        while minHeap:
            weight, dst = heapq.heappop(minHeap)

            if shortest[dst] != -1:
                continue
            shortest[dst] = weight
            for wt2, neightbour in adj[dst]:
                heapq.heappush(minHeap, (weight+wt2, neightbour))
        
        currMax = 0
        for i in shortest:
            if shortest[i] == -1:
                return -1
            if shortest[i] > currMax:
                currMax = shortest[i]
        
        return currMax



        
        