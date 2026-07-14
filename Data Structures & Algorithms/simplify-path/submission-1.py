class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        newpath = path.split('/')
        for obj in newpath:
            if obj == '.' or obj == '':
                continue
            
            elif obj == '..':
                if len(stack) != 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(obj)

        return '/'+'/'.join(stack)
