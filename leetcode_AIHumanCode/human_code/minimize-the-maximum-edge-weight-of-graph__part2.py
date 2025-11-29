# Time:  O(nlogn + e)
# Space: O(n + e)
import collections
import heapq


# prim's algorithm
class Solution2(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        """
        def prim():
            best = [float("inf")]*len(adj)
            min_heap = [(0, 0)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if best[u] != float("inf"):
                    continue
                best[u] = curr
                for v, w in adj[u].items():
                    if best[v] != float("inf"):
                        continue
                    heapq.heappush(min_heap, (w, v))
            result = max(best)
            return result if result != float("inf") else -1

        adj = [collections.defaultdict(lambda: float("inf")) for _ in range(n)]
        for i, j, w in edges:
            adj[j][i] = min(adj[j][i], w)
        return prim()


