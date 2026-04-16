class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxarea = 0
        # for i in range(len(heights)-1):
        #     j = i+1
        #     while j < len(heights):
        #         curr_area = (j - i) * min(heights[i], heights[j])
        #         maxarea = max(maxarea, curr_area)
        #         j += 1
        # return maxarea


        l = 0
        r = len(heights) - 1
        max_ar = 0
        while l < r:
            curr_height = (r - l) * min(heights[l], heights[r])
            max_ar = max(max_ar, curr_height)
            print(f"current height = {curr_height} for {l, r} and heights {heights[l], heights[r]}")
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_ar



