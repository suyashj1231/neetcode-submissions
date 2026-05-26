class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_to_chr = {i: chr(ord('A')+i) for i in range(26)}
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            ans += num_to_chr[rem]
            columnNumber = columnNumber // 26
        return ans[::-1]