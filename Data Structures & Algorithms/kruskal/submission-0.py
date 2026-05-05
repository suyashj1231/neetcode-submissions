class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n


    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self,x , y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.size[rootx] < self.size[rooty]:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            else:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # edges - src, dst, wt
        # heap - wt, src, dst

        minheap = []
        mst = 0
        total = 0
        for s, d, w in edges:
            heapq.heappush(minheap, [w,s,d])
        
       # in heap u added em all make a unionfind
        unionfind = UnionFind(n)
       # popping time
        while minheap:
            weight, n1, n2 = heapq.heappop(minheap)
            if not unionfind.union(n1,n2):
                continue
            mst += weight
            total += 1
        return mst if total == n-1 else -1


