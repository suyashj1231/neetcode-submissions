class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store = {}
        for i in range(len(strs)):
            a = ''.join(sorted(strs[i]))
            if a in store:
                store[a] = store[a]+[strs[i]]
            else:
                store[a] = [strs[i]]

        return store.values()