class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0
        r = len(height) - 1
        rmax = lmax = 0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            
            if lmax<rmax:
                l+=1
                lmax = max(lmax, height[l])
                total += lmax - height[l]
            
            else:
                r-=1
                rmax = max(rmax, height[r])
                total += rmax - height[r]
        
        return total
            
            
            

            





        # curr_max = 0
        # for i in range(len(height)):
        #     curr_max = max(curr_max, height[i])
        #     maxl.append(curr_max)

        # curr_max = 0
        # for i in range(len(height)-1,-1,-1):
        #     curr_max = max(curr_max, height[i])
        #     maxr.append(curr_max)
        
        # maxr.reverse()
        
        # for i in range(len(height)):
        #     total += min(maxl[i], maxr[i]) - height[i]
        
        # return total
        

                
