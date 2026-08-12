from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()
        total = 0
        

        for i in range(n):
            if i in visited:
                continue
    
            queue = deque()
            queue.append(i)
            while queue:
                curr = queue.popleft()
                visited.add(curr)
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            total+=1
        return total
            


