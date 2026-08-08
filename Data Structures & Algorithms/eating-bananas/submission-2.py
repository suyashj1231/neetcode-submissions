class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l<=r:
            m = l +(r-l) // 2 # m is the rate
            hr = 0
            for i in piles:
                hr += -(i // -m)

            if hr <= h:
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1

        return ans
                

        