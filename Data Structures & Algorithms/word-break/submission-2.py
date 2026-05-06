class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {}
        def memoization(i):
            if i == len(s):
                return True
            
            if i in seen:
                return seen[i]

            j = 1
            seen[i] = False
            while i+j <= len(s):
                if s[i:i+j] in wordDict:
                    check = memoization(i+j)
                    if check:
                        seen[i] = check
                j = j + 1
            return seen[i]
        return memoization(0)


        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     if i > len(s):
        #         return False
            
        #     j = 1
        #     while i+j <= len(s):
        #         if s[i:i+j] in wordDict:
        #             if dfs(i+j):
        #                 return True
        #         j = j + 1
        #     return False
        

        # return dfs(0)
