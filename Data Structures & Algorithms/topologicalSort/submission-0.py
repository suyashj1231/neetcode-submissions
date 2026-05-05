class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # eges - src, dst
        adj = {}


        for i in range(n):
            adj[i] = []
        
        for src, dst in edges:
            adj[src].append(dst)
        
        topSort = []
        visited = set()
        path = set()

        def dfs(src):
            if src in path:
                return False
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)

            for neighbour in adj[src]:
               if not dfs(neighbour):
                return False
            topSort.append(src)
            path.remove(src)
            return True


        for i in range(n):
            if dfs(i) is False:
                return []
        
        topSort.reverse()
        return topSort


