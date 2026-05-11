class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        num = n
        while True:
            summer = sum(int(d)**2 for d in str(num))

            if summer in visited:
                return False

            if summer == 1:
                return True
                
            num = summer
            visited.add(summer)

