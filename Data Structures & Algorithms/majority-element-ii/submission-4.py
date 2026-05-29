class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        for n in nums:
            if n in res:
                continue

            if nums.count(n) > len(nums) // 3:
                res.add(n)
        
        return list(res)