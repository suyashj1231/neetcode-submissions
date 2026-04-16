class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in setnum:
                l = 0
                while (i + l) in setnum:
                    l +=1
                longest = max(longest, l)
        return longest




        # set_num = set(nums)
        # maxi = 0
        # for i in set_num:
        #     j =i-1
        #     temp_max = 1
        #     while True:
        #         if j in set_num:
        #             temp_max +=1
        #             j = j - 1
        #         else:
        #             maxi = max(maxi, temp_max)
        #             break

        # return maxi
            


                


