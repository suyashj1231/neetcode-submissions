from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_set = Counter(s)
        s_set = Counter(t)
        return s_set == f_set
        