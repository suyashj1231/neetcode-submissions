class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ""

        for i in range(len(s)):
            for j in range(2):
                l = i
                r = i+j
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        curr = r-l+1
                        if curr>= longest:
                            longest = curr
                            res = s[l:r+1]
                    else:
                        break
                    l-=1
                    r+=1
        
        return res