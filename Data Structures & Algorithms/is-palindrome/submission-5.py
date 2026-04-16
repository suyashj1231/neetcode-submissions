class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean+=i
        
        left = 0
        right = len(clean) - 1
        
        while left < right:
            if clean[left].lower() == clean[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True
        