
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = {}
        for i in hand:
            freq[i] = freq.get(i,0) + 1
        while freq:
            init = next(iter(freq))
            for i in range(groupSize):
                nextval = init + i
                if (nextval) not in freq:
                    return False
                freq[nextval] -= 1
                if freq[nextval] == 0:
                    del(freq[nextval])
        return True

            
        
        