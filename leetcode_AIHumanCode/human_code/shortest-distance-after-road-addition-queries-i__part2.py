# Time:  O(n^2 * logn)
# Space: O(n^2)
import heapq


# dijkstra's algorithm
class Solution2(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        """
        def dijkstra(u, v):
            adj[u].append((v, 1))
            min_heap = [(dist[u], u)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr > dist[u]:
                    continue
                for v, w in adj[u]:
                    if curr+w >= dist[v]:
                        continue
                    dist[v] = curr+w
                    heapq.heappush(min_heap, (dist[v], v))
            return dist[-1]

        adj = [[] for _ in range(n)]
        for u in range(n-1):
            adj[u].append((u+1, 1))
        dist = list(range(n))
        return [dijkstra(u, v) for u, v in queries]
