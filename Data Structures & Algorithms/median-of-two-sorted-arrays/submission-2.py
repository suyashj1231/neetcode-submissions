class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A,B = B,A

        total = len(A) + len(B)
        half = total // 2

        # we do BS on A
        l = 0 
        r = len(A)-1
        while True:
            i = l + (r-l) // 2 # mid for A
            j = half - i-2 # mid for B

            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if i+1<len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if j+1<len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1: # odd
                    return min(Aright, Bright)
                else: # even
                    return (max(Aleft,Bleft)+ min(Aright, Bright)) / 2
            
            elif Aleft > Bright: # partiotion for a is bigger so reduce
                r = i - 1 # r = mid - 1
            
            else: # Aleft > Bright # partiotion for a is smoller so inc
                l = i + 1




    