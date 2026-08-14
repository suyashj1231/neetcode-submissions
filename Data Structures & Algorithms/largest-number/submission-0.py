from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        digits = [str(x) for x in nums]
        def compare(a,b):
            if a + b > b + a:
                return -1
            else:
                return 1

        digits.sort(key=cmp_to_key(compare))
        ans = str(int("".join(digits))) # coz "000" is wrong - so we convet to int and then back str
        return ans