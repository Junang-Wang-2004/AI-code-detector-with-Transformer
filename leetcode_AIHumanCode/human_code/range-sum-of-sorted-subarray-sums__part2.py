# Time:  O(rlogr), worst: O(n^2 * logn)
# Space: O(n)
import heapq


# heap solution
class Solution2(object):
    def rangeSum(self, nums, n, left, right):
        """
        """
        MOD = 10**9+7
        min_heap = []
        for i, num in enumerate(nums, 1):
            heapq.heappush(min_heap, (num, i))
        result = 0
        for i in range(1, right+1):
            total, j = heapq.heappop(min_heap)
            if i >= left:
                result = (result+total)%MOD
            if j+1 <= n:
                heapq.heappush(min_heap, (total+nums[j], j+1))
        return result
