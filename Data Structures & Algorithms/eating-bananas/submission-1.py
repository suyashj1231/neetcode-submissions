class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        ans = r

 # ceil -(a // -b)
        while l <=r:
            m = l + (r-l) // 2

            hr = 0
            for i in piles:
                hr += -(i//-m)
            
            if hr <=h:
                ans = min(ans, m)
                r = m - 1

            else:
                l = m + 1
                
        return ans


            


