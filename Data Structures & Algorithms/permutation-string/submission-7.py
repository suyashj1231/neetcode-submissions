class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {i:0 for i in "abcdefghijklmnopqrstuvwxyz"}
        d2 = {i:0 for i in "abcdefghijklmnopqrstuvwxyz"}

        for i in s1:
            d1[i] += 1

        l = 0
        for r in range(len(s2)):
            d2[s2[r]] +=1
            if (r-l+1) == len(s1):
                if d1 == d2:
                    return True

                d2[s2[l]] -=1
                l+=1
        
        return False