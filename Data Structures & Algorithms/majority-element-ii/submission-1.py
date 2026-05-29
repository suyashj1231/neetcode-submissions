class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        floor = len(nums) // 3
        seen = {}
        ans = set()
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

            if seen[i] > floor:
                    ans.add(i)
        
        return list(ans)