from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        defDict = defaultdict(int)
        for number in nums:
            defDict[number] += 1
        return sorted(defDict, key=defDict.get, reverse=True)[:k]

       
       
       
       
       
       
       
       
       
       
       
       
       # lead = 0 # element
        # counter = 0
        # for i in nums:
        #     if counter <=0 :
        #         lead = i
        #         counter = 1
        #     elif i == lead:
        #         counter += 1
        #     else:
        #         counter -= 1
        # return [lead]