# Time:  O(n + klogn)
# Space: O(1)
import heapq


# heap
class Solution3(object):
    def maximumProduct(self, nums, k):
        """
        """
        MOD = 10**9+7
        min_heap = nums
        heapq.heapify(min_heap)
        while k:
            heapq.heappush(min_heap, heapq.heappop(min_heap)+1)
            k -= 1
        return reduce(lambda x, y: x*y%MOD, min_heap)
