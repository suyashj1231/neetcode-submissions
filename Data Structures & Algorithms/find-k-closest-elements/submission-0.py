class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pre = []
        for i in range(len(arr)):
            pre.append([abs(arr[i]-x), arr[i]])
        
        pre.sort()
        ans = []
        for i in range(k):
            ans.append(pre[i][1])
        ans.sort()
        return ans
