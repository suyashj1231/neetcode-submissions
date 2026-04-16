class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for i in strs:
            enc_str = enc_str + i + "|"
        print(enc_str)

        return enc_str


    def decode(self, s: str) -> List[str]:
        dec_str = []
        word = ""
        for i in s:
            word = word + i
            if i == '|':
                dec_str.append(word[0:-1])
                word = ""
        print(dec_str)
        return dec_str
            
