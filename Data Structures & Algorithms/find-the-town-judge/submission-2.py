
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustRating = {i:0 for i in range(1,n+1)}
        for ai,bi in trust:
            trustRating[bi] +=1
            trustRating[ai] -=1
        
        for key, value in trustRating.items():
            if value == n-1:
                return key
        
        return -1
        
        
            