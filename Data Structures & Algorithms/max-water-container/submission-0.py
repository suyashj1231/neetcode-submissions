class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        current_max=0

        while r > l:
            current_max = max(current_max,self.area(min(heights[l], heights[r]),r-l))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return current_max

    def area(self,l,b):
        return l*b

        
        