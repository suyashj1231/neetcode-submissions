class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = set()
        l=0
        maxval=0

        for i in range(len(s)):
            while s[i] in words:
                words.remove(s[l])
                l+=1
            words.add(s[i])
            maxval = max(maxval, i - l +1 )
        
        return maxval