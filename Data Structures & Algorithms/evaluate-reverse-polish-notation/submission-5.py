class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i =='+':
                    stack.append(a+b)
                if i =='-':
                    stack.append(a-b)
                if i =='*':
                    stack.append(a*b)
                if i =='/':
                    stack.append(int(a / b))
                print(stack[-1])
        return stack[-1]
        
        