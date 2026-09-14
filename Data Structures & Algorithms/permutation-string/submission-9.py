class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_cnt = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}
        s2_cnt = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}

        for i in range(len(s1)):
            s1_cnt[s1[i]] += 1
            s2_cnt[s2[i]] += 1
        
        matches = 0
        for i in "abcdefghijklmnopqrstuvwxyz":
            if s1_cnt[i] == s2_cnt[i]:
                matches+=1

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            s2_cnt[s2[r]] += 1
            if s2_cnt[s2[r]] == s1_cnt[s2[r]]:
                matches +=1
            elif s2_cnt[s2[r]] == s1_cnt[s2[r]] + 1: # previous they were correct match
                matches -=1
            
            s2_cnt[s2[l]] -= 1
            if s2_cnt[s2[l]] == s1_cnt[s2[l]]:
                matches +=1
            elif s2_cnt[s2[l]] == s1_cnt[s2[l]] - 1: # previous they were correct match
                matches -=1
            l+=1
        return matches == 26


