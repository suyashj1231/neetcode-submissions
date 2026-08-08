class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A)>len(B): # let A be smol
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2
    
        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2 # mid of A
            j = half -i -2 # mid of B partiona

            Aleft = A[i] if i >=0 else float('-inf')
            Aright = A[i+1] if i+1 < len(A) else float('inf')
            Bleft = B[j] if j >=0 else float('-inf')
            Bright = B[j+1] if j+1 < len(B) else float('inf')

            if Aleft <= Bright and Aright >= Bleft:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)

                return (min(Aright, Bright) + max(Aleft, Bleft))/2
            
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
        