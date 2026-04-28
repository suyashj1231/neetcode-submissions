class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        lenstr = len(s)

        for i in range(lenstr):
            l,r=i,i
            while l >= 0 and r < lenstr and s[l] == s[r]:
                if (r-l+1) > reslen:
                    reslen = r-l+1
                    res = s[l:r+1]

                l-=1
                r+=1
            
            l,r =i ,i+1
            while l >= 0 and r < lenstr and s[l] == s[r]:
                if (r-l+1) > reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1

        return res



