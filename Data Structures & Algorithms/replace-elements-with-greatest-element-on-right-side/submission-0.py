class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1] * len(arr)
        currmax = -1
        for i in range(len(ans)-2, -1, -1):
            if arr[i+1] > currmax:
                currmax = arr[i+1]
            ans[i] = currmax
        
        return ans