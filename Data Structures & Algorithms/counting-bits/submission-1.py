class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [] 
        for num in range(0, n+1):
            res = 0
            while num:
                num = num & (num-1)
                res+=1
            result.append(res)
        return result