class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sqofdigits(n)

        while slow!=fast:
            slow = self.sqofdigits(slow)
            fast = self.sqofdigits(fast)
            fast = self.sqofdigits(fast)
            
        return fast == 1
        # seen = set()

        # while n not in seen:
        #     seen.add(n)
        #     n = self.sqofdigits(n)

        #     if n == 1:
        #         return True

        # return False

    def sqofdigits(self, n:int):
        val = 0
        while n:
            digit = n % 10
            digit = digit**2
            val += digit
            n = n // 10
        return val
        