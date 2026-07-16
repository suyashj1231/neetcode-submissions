class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: 
            return nums
        def mergeSort(arr, l, r):
            if l == r:
                return arr

            mid = l + (r-l)//2

            mergeSort(arr, l,mid)
            mergeSort(arr, mid+1, r)
            self.merge(arr, l, mid, r)
            return arr
        
        return mergeSort(nums, 0, len(nums)-1)

    
    def merge(self, arr,l,mid,r):
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]

        m = len(left) - 1
        n = len(right) - 1
        last = r

        while m >=0 and n >=0:
            if left[m] > right[n]:
                arr[last] = left[m]
                m-=1
            else:
                arr[last] = right[n]
                n-=1

            last -=1
        
        while m>=0:
            arr[last] = left[m]
            m-=1
            last -=1
        
        while n>=0:
            arr[last] = right[n]
            n-=1
            last -=1
        

        






