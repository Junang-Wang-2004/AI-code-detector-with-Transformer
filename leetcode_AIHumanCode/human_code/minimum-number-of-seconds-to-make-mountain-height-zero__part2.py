# Time:  O(hlogn)
# Space: O(n)
import heapq


# heap
class Solution2(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        """
        min_heap = [(0+1*t, i, 1) for i, t in enumerate(workerTimes)]
        heapq.heapify(min_heap)
        for _ in range(mountainHeight):
            result, i, x = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (result+(x+1)*workerTimes[i], i, x+1))
        return result
