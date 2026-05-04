class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
         # if any is greater than target remove it

        goodtrip = set()
        for triplet in triplets:
            if (triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                continue
            
            for i, v in enumerate(triplet):
                if v == target[i]:
                    goodtrip.add(i)
            
        return len(goodtrip) == 3


    
