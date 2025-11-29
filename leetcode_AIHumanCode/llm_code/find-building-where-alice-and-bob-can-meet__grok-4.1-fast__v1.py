import heapq

class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        ans = [-1] * len(queries)
        buckets = [[] for _ in range(n)]
        for qidx, (x, y) in enumerate(queries):
            mn, mx = min(x, y), max(x, y)
            if heights[mn] < heights[mx] or mn == mx:
                ans[qidx] = mx
            else:
                buckets[mx].append((heights[mn], qidx))
        pq = []
        for pos in range(n):
            for need, qidx in buckets[pos]:
                heapq.heappush(pq, (need, qidx))
            while pq and pq[0][0] < heights[pos]:
                _, qidx = heapq.heappop(pq)
                ans[qidx] = pos
        return ans
