class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1)*int(num2)) # o(n2)
        ans = 0
        for i in range(len(num2)-1, -1, -1):
            mul = 10**(len(num2) - 1 - i)
            row = 0
            for j in range(len(num1)-1, -1, -1):
                digit = int(num2[i]) * int(num1[j])
                row = row + digit * mul
                mul = mul * 10

            ans = ans + row
        
        return str(ans)
