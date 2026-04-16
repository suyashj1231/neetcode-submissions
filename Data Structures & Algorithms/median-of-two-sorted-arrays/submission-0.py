class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        total = len(nums1) + len(nums2)
        half = total // 2
        l = 0
        r = len(A) - 1
        while True:
            i = (l + r) // 2 # index for A where we take range
            j = half - i - 2 # minus 2 as indexed at 0 for B and A 
            
            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float("-infinity")

            if (i + 1) < len(A):
                Aright = A[i+1]
            else:
                Aright = float("infinity")

            if j >= 0:
                Bleft  = B[j]
            else:
                Bleft = float("-infinity")

            if (j + 1) < len(B):
                Bright = B[j+1]
            else:
                Bright = float("infinity")

        # now bs
        
            if Aleft <= Bright and Bleft <= Aright:
                # odd median
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min (Aright, Bright)) / 2
            elif Aleft > Bright:
                    r = i - 1
            else:
                    l = i + 1

            


        

        
                