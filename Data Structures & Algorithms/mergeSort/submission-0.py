# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def mergeSortfn(pairs):
            if len(pairs) <=1:
                return pairs
            
            mid = len(pairs) // 2

            l = mergeSortfn(pairs[:mid])
            r = mergeSortfn(pairs[mid:])
            return self.merge(l, r)

        return mergeSortfn(pairs)


    def merge(self, left, right):
        l = r = 0
        ans = []
        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                ans.append(left[l])
                l +=1
            else:
                ans.append(right[r])
                r+=1
            
        if l < len(left):
            ans.extend(left[l:])

        if r < len(right):
            ans.extend(right[r:])

        return ans
