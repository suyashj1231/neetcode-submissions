from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s= dict(Counter(s))
        for i in t:
            if i not in s:
                return False
            else:
                if s[i] == 0:
                    return False
                s[i] = s[i] - 1
                
        return True



        