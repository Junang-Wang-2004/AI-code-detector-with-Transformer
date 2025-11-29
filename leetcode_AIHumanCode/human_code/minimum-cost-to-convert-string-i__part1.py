# Time:  O(o + k * eloge + n), k = len(set(original)), e is the number of edges reachable from a given node u
# Space: O(o + k * v), v is the number of nodes reachable from a given node u

import heapq


# dijkstra's algorithm, memoization
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        """
        INF = float("inf")
        def dijkstra(start):
            best = {start:0}
            min_heap = [(0, start)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr > best[u]:
                    continue
                if u not in dist:
                    continue
                for v, w in dist[u].items():     
                    if v in best and best[v] <= curr+w:
                        continue
                    best[v] = curr+w
                    heapq.heappush(min_heap, (best[v], v))
            return best

        memo = {}
        def memoization(u, v):
            if u not in memo:
                memo[u] = dijkstra(u)
            return memo[u][v] if v in memo[u] else INF

        dist = {}
        for i in range(len(original)):
            u, v = ord(original[i])-ord('a'), ord(changed[i])-ord('a')
            if u not in dist:
                dist[u] = {v:INF}
            if v not in dist[u]:
                dist[u][v] = INF
            dist[u][v] = min(dist[u][v], cost[i])
        result = sum(memoization(ord(source[i])-ord('a'), ord(target[i])-ord('a')) for i in range(len(source)))
        return result if result != INF else -1


