from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countList = []
        for i in strs:
            adder = True
            for common in range(len(countList)):
                if Counter(countList[common][0]) == Counter(i):
                    countList[common].append(i)
                    adder = False
                
            if adder:
                countList.append([i])
        
        return countList
            
            