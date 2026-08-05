class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numtodig = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []
        curr = ""
        def backtrack(curr, i):
            if len(curr) == len(digits):
                ans.append(curr)
                return
            
            for char in numtodig[digits[i]]:
                backtrack(curr+char, i+1)
        
        if digits: backtrack(curr,0)
        return ans