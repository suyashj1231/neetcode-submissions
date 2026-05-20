class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:

            if i == "+":    
                b = stack.pop()
                a = stack.pop()
                stack.append(a)
                stack.append(b)
                stack.append(a+b)
            
            elif i == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(a*2)

            elif i == "C":
                if stack:
                    stack.pop()
            else:
                stack.append(int(i))

            print(stack)
        
        return sum(stack)
