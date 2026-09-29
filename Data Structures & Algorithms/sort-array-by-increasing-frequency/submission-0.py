from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        cnt = list(frequency.items())
        cnt.sort(key=lambda x: (x[1], -x[0]))
        res = []
        for char, freq in cnt:
            res.extend([char]*freq)
        
        return res

