from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mArray = {}

        for i in range(len(strs)):
            curr = "".join(sorted(strs[i]))
            if curr in mArray:
                mArray[curr].append(strs[i])
            else:
                mArray[curr] = [strs[i]]
        
        return list(mArray.values())