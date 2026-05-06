class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True
            
            if i > len(s):
                return False
            
            # some condition:
            j = 1
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    if dfs(j):
                        return True
            
            return False
        

        return dfs(0)
