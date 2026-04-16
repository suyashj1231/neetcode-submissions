from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = (Counter(nums)).most_common()
        ans=[]
        print(count)
        for i in range(k):
            ans.append(count[i][0])
        
        return ans


