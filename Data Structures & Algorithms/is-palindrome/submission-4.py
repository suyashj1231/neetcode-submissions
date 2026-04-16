class Solution:
    def isPalindrome(self, s: str) -> bool:
        words =""
        for i in s:
            if i.isalnum():
                words += i.lower()
        l = 0
        r = len(words) - 1
        while l < r:
            if words[l]!=words[r]:
                return False
            l += 1
            r -= 1
    
        return True
        