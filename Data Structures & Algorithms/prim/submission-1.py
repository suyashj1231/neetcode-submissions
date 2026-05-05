class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # edge = src, dst, wt
        # in our heap we sort via wt, sorted
        # minheap = wt, src, dst

        # make adj list to connect nodes amongselves

        adj = {}

        for i in range(n):
            adj[i] = []

        for s, d, w in edges:
            adj[s].append([d,w])
            adj[d].append([s,w])
        
        # connected with wt, now make the minheap and sol
        visited = set()
        minHeap = []
        mst = 0
        total = 1
        # we start with 0, can start with oth too
        for dst, wt in adj[0]:
            heapq.heappush(minHeap,[wt, 0, dst])
        visited.add(0)

        while minHeap:
            weight, src, dst = heapq.heappop(minHeap)
            if dst in visited: # if seen we ignore
                continue
            
            visited.add(dst) # if not we add that edge
            mst += weight
            total += 1 # count num of nodes we add in mst
            for neighbour, w in adj[dst]:
                if neighbour not in visited:
                    heapq.heappush(minHeap,[w, dst, neighbour])
        
        return mst if total == n else -1


            
