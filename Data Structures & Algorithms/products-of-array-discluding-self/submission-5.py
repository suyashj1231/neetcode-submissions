class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        pref, suff, res =[0]*arr_len,[0]*arr_len,[0]*arr_len

        pref[0] = 1
        suff[-1] = 1

        for i in range(1,arr_len):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        for i in range(arr_len - 2, -1, -1 ):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(arr_len):
            res[i] = pref[i] * suff[i]

        return res