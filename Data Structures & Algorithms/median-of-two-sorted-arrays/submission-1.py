class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        m = len(nums1)
        n = len(nums2)
        l=r=0
        while l < m and r < n:
            if nums1[l] > nums2[r]:
                ans.append(nums2[r])
                r+=1
            else:
                ans.append(nums1[l])
                l+=1
        
        while l < m:
            ans.append(nums1[l])
            l+=1
        
        while r < n:
            ans.append(nums2[r])
            r+=1
        
        length = len(ans)
        print(length)

        if length % 2 == 0: # even
            a1 = (length-1) // 2 
            a2 = a1+1
            median = (ans[a1] + ans[a2]) / 2
        
        else: # odd
            a1 = (length-1) // 2
            median = (ans[a1])
        
        return median


