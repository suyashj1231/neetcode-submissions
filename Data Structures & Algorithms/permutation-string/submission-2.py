from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        a = Counter(s1)
        l=0
        
        while l < len(s2) - len(s1) + 1:
            b = Counter(s2[l:l+len(s1)])
            if a == b:
                return True
            
            l+=1
        return False
        
        


            





        
        

