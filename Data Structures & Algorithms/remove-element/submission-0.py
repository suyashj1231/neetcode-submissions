class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for l in range(len(nums)):
            if nums[l] != val:   # ← condition flipped: keep non-val
                nums[k] = nums[l]
                k += 1

        return k
        