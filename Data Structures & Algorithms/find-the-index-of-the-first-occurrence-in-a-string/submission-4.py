from _heapq import heapify
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #kmp algo rithm
        if needle == '': return 0
        LPS = [0] * len(needle)
        prevLPS =0
        i = 1
        while i < len(needle):
            if needle[prevLPS] == needle[i]:
                LPS[i] = prevLPS + 1
                prevLPS +=1
                i+=1

            elif prevLPS == 0:
                LPS[i] = 0
                i+=1
            else:
                prevLPS = LPS[prevLPS-1]
        
        i=0 # ptr haystack
        j=0 # ptr needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i +=1
                j += 1
            elif j==0:
                i+=1
            else:
                j = LPS[j-1]
            
            if j == len(needle):
                return i - len(needle)
        
        return -1
            








