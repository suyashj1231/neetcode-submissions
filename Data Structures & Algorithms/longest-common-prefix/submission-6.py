class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if not strs:
            return ""
        ans = strs[0]
        for new in range(1, len(strs)):
            l = 0
            while l < min(len(ans),len(strs[new])):
                if ans[l] == strs[new][l]:
                    l+=1
                else:
                    break
            ans = ans[0:l]
        
        return ans