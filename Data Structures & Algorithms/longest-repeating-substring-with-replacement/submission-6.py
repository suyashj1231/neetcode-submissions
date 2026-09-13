class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}        
        l = 0
        ans = 0
        for r in range(len(s)):
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1
            maxf = max(charFreq.values())
            while (r-l+1) - maxf > k:
                charFreq[s[l]] -= 1
                l +=1
            ans = max(ans, r-l+1)
        
        return ans
            
            

        