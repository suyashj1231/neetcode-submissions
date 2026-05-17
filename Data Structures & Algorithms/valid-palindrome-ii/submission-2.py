class Solution:
    def validPalindrome(self, s: str) -> bool:
        posDel = 1
        l = 0
        r = len(s) - 1

        while l <=r:
            if s[l] != s[r]:
                return (self.is_palindrome(s[l+1:r+1]) or 
                self.is_palindrome(s[l:r]))
            l += 1
            r -= 1
        return True
    
    def is_palindrome(self, sub) -> bool:
        l = 0
        r = len(sub)-1
        while l <=r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        return True

