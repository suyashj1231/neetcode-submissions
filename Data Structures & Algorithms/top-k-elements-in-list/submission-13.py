from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        arranged = [item[0] for item in count.most_common()]
        return arranged[0:k]

        