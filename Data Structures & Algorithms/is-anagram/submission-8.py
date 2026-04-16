from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# S1
        # return (sorted(s) == sorted(t))

# S2
        dict1 = Counter(s)
        dict2 = Counter(t)

        return dict1 == dict2

        