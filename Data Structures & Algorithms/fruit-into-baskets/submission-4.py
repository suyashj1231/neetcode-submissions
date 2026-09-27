class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = defaultdict(int) # fruitype : counts
        l = 0
        res= 0
        for r in range(len(fruits)):
            types[fruits[r]] += 1
            while len(types)>2:
                f = fruits[l]
                types[f] -= 1
                if types[f] == 0:
                    types.pop(f)
                l+=1
            res = max(res, r-l+1)
        return res