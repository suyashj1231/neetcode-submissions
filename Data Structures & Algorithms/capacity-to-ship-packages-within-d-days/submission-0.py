class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r

        while l <=r:
            m = l + (r-l)//2

            ships = 1
            curr = m
            for i in weights:
                if (curr - i) < 0:
                    ships +=1
                    curr = m
                curr -= i
            
            if ships <= days:
                ans = min(ans,m)
                r = m - 1
            else:
                l = m + 1

        return ans
            
                

            
            



                

