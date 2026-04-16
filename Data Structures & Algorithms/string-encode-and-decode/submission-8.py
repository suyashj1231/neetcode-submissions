class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for i in strs:
            enc_str = enc_str + str(len(i)) + "#" + i
        
        return enc_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


