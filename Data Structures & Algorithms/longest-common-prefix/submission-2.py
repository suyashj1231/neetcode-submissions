class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        start = strs[0]
        end = strs[-1]
        l,r =0,0

        while l<len(start) and l < len(end):
            if start[l] == end[l]:
                l+=1
            else:
                break
        
        return start[0:l]