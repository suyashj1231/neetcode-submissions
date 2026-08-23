# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0

        for i in range(1,n):
            if knows(candidate, i):
                candidate = i

        if self.isceleb(candidate,n):
            return candidate
        else:
            return -1

    def isceleb(self,candidate,n):
        for i in range(n):
            if i == candidate:
                continue

            elif not knows(i,candidate) or knows(candidate,i):
                return False
        return True