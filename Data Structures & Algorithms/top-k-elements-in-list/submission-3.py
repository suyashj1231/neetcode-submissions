class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fict = {}
        for i in sorted(nums,reverse=True):
            if i in fict:
                fict[i] = fict[i] + 1
            else:
                fict[i] = 1

        fict = (dict(sorted(fict.items(), key=lambda item: item[1], reverse=True)))
        return list(fict.keys())[0:k]

       
       
       
       
       
       
       
       
       
       
       
       
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