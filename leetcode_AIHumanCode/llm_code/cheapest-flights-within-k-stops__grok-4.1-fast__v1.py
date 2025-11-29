import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        INF = float('inf')
        distances = [[INF] * (K + 2) for _ in range(n)]
        distances[src][0] = 0
        pq = [(0, src, 0)]
        while pq:
            cost, node, stops = heapq.heappop(pq)
            if cost > distances[node][stops]:
                continue
            if node == dst:
                return cost
            for nei, wt in graph[node]:
                newstops = stops + 1
                if newstops > K + 1:
                    continue
                newcost = cost + wt
                if newcost < distances[nei][newstops]:
                    distances[nei][newstops] = newcost
                    heapq.heappush(pq, (newcost, nei, newstops))
        return -1
