class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for i in nums: # get freq count
            count[i] = count.get(i,0) + 1

        for key, val in count.items(): # map freq to key
            bucket[val].append(key)
        
        ans = []
        for val in range(len(bucket)-1, -1, -1):
            for term in bucket[val]:
                ans.append(term)
                if len(ans) == k:
                    return ans
        
        

        



        

        