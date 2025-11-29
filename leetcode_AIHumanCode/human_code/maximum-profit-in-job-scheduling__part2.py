# Time:  O(nlogn)
# Space: O(n)
import heapq
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        """
        min_heap = list(zip(startTime, endTime, profit))
        heapq.heapify(min_heap)
        result = 0
        while min_heap:
            s, e, p = heapq.heappop(min_heap)
            if s < e:
                heapq.heappush(min_heap, (e, s, result+p))
            else:
                result = max(result, p)
        return result
