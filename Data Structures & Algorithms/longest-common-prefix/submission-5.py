class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        start = strs[0]
        for new in range(1,len(strs)):
            l = 0
            while l<len(strs[new]) and l < len(start):
                if start[l] == strs[new][l]:
                    l+=1
                else:
                    break
    
            start = start[0:l]

        return start
