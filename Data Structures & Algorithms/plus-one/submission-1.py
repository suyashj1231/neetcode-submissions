class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        last = len(digits) - 1
        newnum = 1 + digits[last]
        digits[last] = newnum % 10
        carry = newnum // 10

        while carry:
            if last == 0:
                return [carry] + digits

            newnum = carry + digits[last - 1]

            digits[last - 1] =  newnum % 10 
            carry = newnum // 10
            last = last - 1
        
        return digits


