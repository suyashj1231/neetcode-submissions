class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0

        for i in range(len(heights)-1):
            j = i+1
            while j < len(heights):
                curr_area = (j - i) * min(heights[i], heights[j])
                maxarea = max(maxarea, curr_area)
                j += 1
        return maxarea