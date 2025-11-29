# Time:  O(n + qlogq)
# Space: O(n + q)
import heapq


# offline solution, heap
class Solution2(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        """
        result = [-1]*len(queries)
        qs = [[] for _ in range(len(heights))]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                result[i] = b
            else:
                qs[b].append((heights[a], i))
        min_heap = []
        for i, h in enumerate(heights):
            for q in qs[i]:
                heapq.heappush(min_heap, q)
            while min_heap and min_heap[0][0] < h:
                _, j = heapq.heappop(min_heap)
                result[j] = i
        return result


