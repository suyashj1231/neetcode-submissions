from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        arranged = count.most_common()
        ans = []
        for i in range(k):
            ans.append(arranged[i][0])
        return ans

        