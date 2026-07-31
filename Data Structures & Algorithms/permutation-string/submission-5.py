class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_cnt = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}
        s2_cnt = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}

        for c in s1:
            s1_cnt[c] += 1
        
        l = 0
        for r in range(len(s2)):
            s2_cnt[s2[r]] +=1
            if (r - l + 1) == len(s1): # window eq. size of s1
                if s1_cnt == s2_cnt:
                    return True
                
                else:
                    s2_cnt[s2[l]] -=1
                    l+=1
            
        return False

