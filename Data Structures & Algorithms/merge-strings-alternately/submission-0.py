class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l, r = 0, 0
        
        while l < len(word1) and r < len(word2):
            res += (word1[l])
            res += (word2[r])
            l+=1
            r+=1
        
        if len(word1) > len(word2):
            res = res + word1[l:]
        
        if len(word1) < len(word2):
            res = res + word2[r:]
        
        return res