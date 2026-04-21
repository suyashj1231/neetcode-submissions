class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        numtodig = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        curr = []
        def combination(i):
            if i >= len(digits):
                res.append("".join(curr))
                return
            
            for digit in numtodig[digits[i]]:
                curr.append(digit)
                combination(i+1)
                curr.pop()
        
        combination(0)
        return res
                


