class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ast = 0
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                difference = asteroid + stack[-1]
                if difference > 0:
                    asteroid = 0
                elif difference < 0:
                    stack.pop()
                else:
                    asteroid = 0
                    stack.pop()
            
            if asteroid !=0:
                stack.append(asteroid)
        
        return stack
                    
