class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        
        # Build maxleft
        maxleft[0] = height[0]
        for i in range(1, n):
            maxleft[i] = max(height[i], maxleft[i-1])
        
        # Build maxright
        maxright[-1] = height[-1]
        for i in range(n-2, -1, -1):
            maxright[i] = max(height[i], maxright[i+1])
        
        water = 0

        for i in range(n):
            water += min(maxleft[i], maxright[i]) - height[i]
        
        return water