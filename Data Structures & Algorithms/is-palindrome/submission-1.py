class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        a=''
        for i in range(len(s)):
            if s[i].isalnum():
                a = a+s[i].lower()
        print(a)
        for i in range(len(a)//2):
            front = a[i]
            back = a[len(a)-i-1]
            if front == back:
                pass
            else:
                return False
        return True


    # -2<=x<=2