class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need = len(needle)

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if (i + need) < len(haystack)+1 and haystack[i:i+need] == needle:
                    return i
        
        return -1
