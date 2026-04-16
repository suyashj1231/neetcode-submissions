class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        main = set()

        for i in nums:
            if i in main:
                main.remove(i)
            else:
                main.add(i)
        
        return main.pop()