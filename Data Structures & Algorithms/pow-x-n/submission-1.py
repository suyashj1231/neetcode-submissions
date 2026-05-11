class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = x
        if n == 0:
            return 1
        for i in range(abs(n)-1):
            y = y * x
        if n < 0:
            return 1/y
        return y
            
