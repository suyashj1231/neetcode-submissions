class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for key, val in prerequisites:
            adj_list[key].append(val)
        
        seen = set()
        print(adj_list)
        def dfs(course):
            if course in seen:
                return False
            
            if adj_list[course] == []:
                return True
            
            seen.add(course)
            for prerequisites in adj_list[course]:
                if not dfs(prerequisites):
                    return False

            adj_list[course] = []
            seen.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
