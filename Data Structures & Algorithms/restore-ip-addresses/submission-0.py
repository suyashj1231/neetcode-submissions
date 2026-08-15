class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        ans = []
        def backtrack(index, dots, IP):
            if dots == 4 and index == len(s):
                ans.append(IP[:-1])
                return
            if dots > 4:
                return

            for j in range(index,min(index+3, len(s))):
                if int(s[index:j+1]) < 256 and (index == j or s[index]!='0'):
                    backtrack(j+1, dots+1, IP + s[index:j+1] + '.')

        
        backtrack(0,0,"")
        return ans






            
            
            

            
            

