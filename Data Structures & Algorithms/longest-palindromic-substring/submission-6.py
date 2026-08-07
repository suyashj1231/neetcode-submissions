class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        # odd len and ecen
        longest = ""
        for i in range(len(s)):
            for j in range(2):
                l = i
                r = i +j
                while l >=0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > len(longest):
                        longest = s[l:r+1]

                    l-=1
                    r+=1

        return longest


