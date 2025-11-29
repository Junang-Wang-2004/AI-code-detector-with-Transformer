# Time:  O(nlogk)
# Space: O(k)
import heapq


class Solution2(object):
    def kClosest(self, points, K):
        """
        """
        def dist(point):
            return point[0]**2 + point[1]**2
        
        max_heap = []
        for point in points:
            heapq.heappush(max_heap, (-dist(point), point))
            if len(max_heap) > K:
                heapq.heappop(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(len(max_heap))]
