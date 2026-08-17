class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l=0
        res = 0
        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1

            while len(freq) > 2:
                rem = fruits[l]
                freq[rem] -=1

                if freq[rem] == 0:
                    freq.pop(rem)
                l+=1

            res = max(res, r-l+1)
        return res
                
