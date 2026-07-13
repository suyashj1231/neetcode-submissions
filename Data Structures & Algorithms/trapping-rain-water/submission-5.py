class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        lmax = rmax = 0
        ans = 0

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                l+=1
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
            else:
                r-=1
                rmax = max(rmax, height[r])
                ans += rmax - height[r]

        return ans
