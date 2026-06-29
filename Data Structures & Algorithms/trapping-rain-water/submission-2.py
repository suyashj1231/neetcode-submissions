class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = []
        water_stored = []

        currmax = 0
        for i in range(len(height)):
            currmax = max(height[i], currmax)
            leftmax.append(currmax)
        
        currmax = 0
        for i in range(len(height)-1,-1,-1):
            currmax = max(height[i], currmax)
            rightmax.append(currmax)
        rightmax.reverse()
        for i in range(len(height)):
            water_at = min(leftmax[i], rightmax[i]) - height[i]
            water_stored.append(water_at)
        
        return sum(water_stored)
