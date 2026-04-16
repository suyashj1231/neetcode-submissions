class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)

        maxk = len(nums) - k + 1
        res = 0
        while maxk > 0:
            res = heapq.heappop(minHeap)
            maxk -=1
        return res
