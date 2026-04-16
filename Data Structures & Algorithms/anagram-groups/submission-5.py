from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mArray = {}
        for i in strs:

            current = "".join(sorted(i))
            if current in mArray:
                mArray[current].append(i)
            else:
                mArray[current] = [i]
        
        return list(mArray.values())
    