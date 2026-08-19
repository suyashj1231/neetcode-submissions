class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sqofdigits(n)

            if n == 1:
                return True

        return False

    def sqofdigits(self, n:int):
        val = 0
        while n:
            digit = n % 10
            digit = digit**2
            val += digit
            n = n // 10
        return val
        