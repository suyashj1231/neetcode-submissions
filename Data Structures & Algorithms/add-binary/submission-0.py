class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 0 0 -> 0
        # 1 0 -> 1
        # 0 1 -> 1
        # 1 1 -> 0 + 1 carry
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ""
        while i>=0 or j>=0 or carry:
            if i >= 0:
                a_bit = int(a[i])
            else:
                a_bit = 0
            
            if j >= 0:
                b_bit = int(b[j])
            else:
                b_bit = 0
            
            # now bit logic
            total = a_bit + b_bit + carry
            carry = total // 2
            digit = total % 2
            ans += str(digit)
            i-=1
            j-=1

        return ans[::-1]


