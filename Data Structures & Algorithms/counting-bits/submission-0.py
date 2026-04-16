class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [] 
        for num in range(0, n+1):
            res = 0
            while num:
                res += num % 2
                num = num >> 1
            result.append(res)
        return result