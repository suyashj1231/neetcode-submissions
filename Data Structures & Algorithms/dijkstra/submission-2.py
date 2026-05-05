class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        shortest = {}

        for i in range(n):
            adj[i] = []
            shortest[i] = -1

        for s, d, w in edges:
            adj[s].append((d,w))
        
        minHeap = [(0, src)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if shortest[n1]!= -1:
                continue
            
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if shortest[n2] == -1:
                    heapq.heappush(minHeap, (w1+ w2, n2))
            
        return shortest

            







