class Solution:
    def mySqrt(self, x: int) -> int:
        end = x // 2
        l = 0
        r = end
        if x == 1:
            return 1
        while l <= r:
            mid = (l + (r-l) // 2)

            if mid*mid > x:
                r = mid - 1
            
            elif mid*mid < x:
                l = mid + 1
                ans = mid
            
            else:
                return mid
        
        return ans