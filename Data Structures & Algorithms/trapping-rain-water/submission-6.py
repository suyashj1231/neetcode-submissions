class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        maxl = []
        maxr = []

        curr_max = 0
        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            maxl.append(curr_max)

        curr_max = 0
        for i in range(len(height)-1,-1,-1):
            curr_max = max(curr_max, height[i])
            maxr.append(curr_max)
        
        maxr.reverse()
        
        for i in range(len(height)):
            total += min(maxl[i], maxr[i]) - height[i]
        
        return total
        

                
