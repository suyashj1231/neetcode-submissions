from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = sorted(Counter(nums).items(), key=lambda item: item[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(elements[i][0])

        return ans

