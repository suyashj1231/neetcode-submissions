class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        l = 0
        newpath = path.split('/')
        print(newpath)
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
