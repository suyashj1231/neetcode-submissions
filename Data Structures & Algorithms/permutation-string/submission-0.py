from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        window = len(s1)
        l = 0
        winset = Counter(s1)
        for r in range(len(s2)):
            if s2[r] in s1:
                l = r
                r = r + window
                if winset == Counter(s2[l:r]):
                    return True
        return False
            
