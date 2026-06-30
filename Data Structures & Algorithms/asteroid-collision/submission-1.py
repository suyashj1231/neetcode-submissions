class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ast = 0
        while ast < len(asteroids):
            stack.append(asteroids[ast])
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                    a = stack.pop()
                    b = stack.pop()
                    if abs(a) > abs(b):
                        stack.append(a)
                    elif abs(a) < abs(b):
                        stack.append(b)
                    else:
                        pass
            ast += 1
        
        return stack
    
