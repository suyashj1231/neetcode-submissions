class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowsFreq = {}
        tFreq = {}
        for i in t:
            tFreq[i] = tFreq.get(i,0) + 1
        needed = len(tFreq)
        have = 0
        ans = (-1,-1)
        ansLen = float('inf')
        l = 0
        r= 0
        for r in range(len(s)):
            windowsFreq[s[r]] = windowsFreq.get(s[r],0) + 1
            if s[r] in tFreq and windowsFreq[s[r]] == tFreq[s[r]]:
                    have += 1

            while have == needed:
                if (r-l+1) < ansLen:
                    ans = [l,r]
                    ansLen = r-l+1
                windowsFreq[s[l]] -= 1
                if s[l] in tFreq and windowsFreq[s[l]] < tFreq[s[l]]:
                    have -= 1
                l+=1

        l,r = ans
        return s[l:r+1]

                    

                    


        

