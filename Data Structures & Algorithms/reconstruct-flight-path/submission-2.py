class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # src = JFK
    # no invalid cases
    # tickets - [src, des]
    # valid mst
    # no union Find though so use kruskals
        adj = {}
        tickets.sort()

        for src, dst in tickets:
            adj[src] = adj.get(src, []) + [dst]
        
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj: # no out edges
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp): # going through neighbour and remove that index we visited
                # go that path
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                #cleanup
                adj[src].insert(i,v)
                res.pop(-1)
            return False
            
        dfs('JFK')
        return res
            

