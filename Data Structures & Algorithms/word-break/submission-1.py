class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True
            
            if i > len(s):
                return False
            
            # some condition:
            j = 1
            while i+j <= len(s):
                if s[i:i+j] in wordDict:
                    if dfs(i+j):
                        return True
                j= j + 1
            return False
        

        return dfs(0)
