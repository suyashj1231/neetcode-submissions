class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col_map = {i: chr(ord('A') + i) for i in range(26)}
        ans = ""

        while columnNumber > 0:
            columnNumber = columnNumber - 1
            curr = columnNumber % 26
            ans+= col_map[curr]
            columnNumber = columnNumber // 26

        return ans[::-1]