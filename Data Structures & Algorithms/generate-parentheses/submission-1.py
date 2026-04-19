class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub = []
        cur = []
        start = 0
        close = 0
        def helper(start,close):
            if start == close == n:
                sub.append("".join(cur))
                return
            
            if start < n:
                cur.append('(')
                helper(start+1, close)
                cur.pop()

            if close < start:
                cur.append(')')
                helper(start,close+1)
                cur.pop()

        helper(0,0)
        return sub
                