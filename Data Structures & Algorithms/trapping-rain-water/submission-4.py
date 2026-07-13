class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = []

        curr_max = 0
        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            leftmax.append(curr_max)
        
        curr_max = 0
        for i in range(len(height)-1, -1, -1):
            curr_max = max(curr_max, height[i])
            rightmax.append(curr_max)
        
        rightmax.reverse()
        ans = 0
        for i in range(len(height)):
            ans += min(rightmax[i],leftmax[i]) - height[i]

        return ans