class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr = set()
        ans = 0
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l+=1
            curr.add(s[r])
            ans = max(ans,r-l+1)
        return ans