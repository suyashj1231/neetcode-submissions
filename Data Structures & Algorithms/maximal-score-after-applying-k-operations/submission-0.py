import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        total = 0
        while k > 0:
            curr = heapq.heappop_max(heap)
            total += curr
            curr = math.ceil(curr/3)
            heapq.heappush_max(heap,curr)
            k-=1
        return total



