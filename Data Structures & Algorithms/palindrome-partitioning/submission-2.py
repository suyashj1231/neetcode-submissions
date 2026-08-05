class Solution:
    def is_palindrome(self, strs, l, r):
        while l < r:
            if strs[l] != strs[r]:
                return False
            l+=1
            r-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currset=[]
        def dfs(i):
            if i >= len(s):
                res.append(currset.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_palindrome(s,i,j):
                    currset.append(s[i:j+1])
                    dfs(j+1)
                    currset.pop()

        dfs(0)
        return res
            
                

    

