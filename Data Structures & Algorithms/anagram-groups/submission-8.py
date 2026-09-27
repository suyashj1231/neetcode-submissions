from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            cnt = "".join(sorted(word))
            if cnt in anagrams:
                anagrams[cnt] = anagrams[cnt] + [word]
            else:
                anagrams[cnt] = [word]

        return list(anagrams.values())