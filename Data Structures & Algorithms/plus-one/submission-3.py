class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits) - 1
        newnum = digits[last] + 1
        digits[last] = newnum % 10
        carry = newnum // 10

        while carry:
            if last == 0:
                return [carry] + digits
                
            newnum = digits[last-1] + 1

            digits[last-1] = newnum % 10

            carry = newnum // 10

            last -= 1
            
        return digits

            