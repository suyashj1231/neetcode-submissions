class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == ']':
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False
            
            elif i == ')':
                if stack and stack.pop() == '(':
                    continue
                else:
                    return False
            
            elif i == '}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False
            else:
                stack.append(i)
        
        if stack:
            return False
            
        return True