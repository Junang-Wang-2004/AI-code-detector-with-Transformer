# Time:  O(n + klogn)
# Space: O(n)
import heapq


# simulation, heap
class Solution4(object):
    def getFinalState(self, nums, k, multiplier):
        """
        """
        if multiplier == 1:
            return nums
        min_heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(min_heap)
        for _ in range(k):
            i = heapq.heappop(min_heap)[1]
            nums[i] *= multiplier
            heapq.heappush(min_heap, (nums[i], i))
        return nums


