from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# s1  
        # viewed = {}
        # for i in nums:
        #     if i in viewed:
        #         viewed[i] = viewed[i] + 1
        #     else:
        #         viewed[i] = 1
        
        # arranged = sorted(viewed, key=viewed.get, reverse=True)
        # return arranged[:k]

# s2
        viewed = {}
        for i in nums:
            viewed[i] = 1 + viewed.get(i,0)

        sorted_arr =[]
        for i,j in viewed.items():
            sorted_arr.append([j,i])
        sorted_arr.sort()
        res = []

        while len(res) < k:
            res.append(sorted_arr.pop()[1])
        return res

        

        






        