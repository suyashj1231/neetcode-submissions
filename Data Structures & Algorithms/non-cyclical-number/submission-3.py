class Solution:
    def isHappy(self, n: int) -> bool:
        slow = sum(int(x)**2 for x in str(n))
        fast = sum(int(x)**2 for x in str(slow))

        while slow != fast:
            slow = sum(int(x)**2 for x in str(slow))
            fast = sum(int(x)**2 for x in str(fast))
            fast = sum(int(x)**2 for x in str(fast))
        
        return slow == 1


