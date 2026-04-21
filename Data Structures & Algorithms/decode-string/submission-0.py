class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                curr = ""
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                
                stack.append(int(multiplier) * curr)
        
        return "".join(stack)

            
        