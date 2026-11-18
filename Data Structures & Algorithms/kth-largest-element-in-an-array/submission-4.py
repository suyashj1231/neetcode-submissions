class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        ans = 0
        while k > 0 and heap:
            ans = heapq.heappop_max(heap)
            k -= 1
        return ans