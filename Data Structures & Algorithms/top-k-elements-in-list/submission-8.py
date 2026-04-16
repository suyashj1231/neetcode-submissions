from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        viewed = {}
        for i in nums:
            if i in viewed:
                viewed[i] = viewed[i] + 1
            else:
                viewed[i] = 1
        
        arranged = sorted(viewed, key=viewed.get, reverse=True)
        return arranged[:k]




        