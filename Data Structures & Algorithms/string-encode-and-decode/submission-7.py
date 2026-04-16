class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            length = str(len(i))
            packet = length + '#' + i
            encoded += packet
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i =0 
        while i < len(s):
            haser = s.find('#', i)
            size = int(s[i:haser])
            dec_str = s[haser+1:haser+size+1]
            decoded.append(dec_str)
            i = haser + 1 + size
        return decoded
        
        return res
                
            
