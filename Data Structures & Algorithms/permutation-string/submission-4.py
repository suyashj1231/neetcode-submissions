class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_cnt = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}
        s2_cnt = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}

        for i in range(len(s1)): # add char to dict and also check the 1st window

            s1_cnt[s1[i]] += 1
            s2_cnt[s2[i]] += 1
        
        matches = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if s1_cnt[i] == s2_cnt[i]:
                matches +=1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # add to right side of window
            curr = s2[r]
            s2_cnt[curr] += 1

            if s1_cnt[curr] == s2_cnt[curr]:
                matches +=1
            
            elif s1_cnt[curr] + 1 == s2_cnt[curr]:
                matches -=1
            
            curr = s2[l]
            s2_cnt[curr] -= 1

            if s1_cnt[curr] == s2_cnt[curr]:
                matches +=1
            
            elif s1_cnt[curr] - 1 == s2_cnt[curr]:
                matches -=1
            
            l += 1
        
        return matches == 26
            

            
            
            
        
        



        
        