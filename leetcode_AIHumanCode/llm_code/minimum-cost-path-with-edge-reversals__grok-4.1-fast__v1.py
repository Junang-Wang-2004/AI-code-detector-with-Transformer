import heapq

class Solution:
    def minCost(self, n, edges):
        graph = [[] for _ in range(n)]
        for start, end, cost in edges:
            graph[start].append((end, cost))
            graph[end].append((start, cost * 2))
        costs = [float('inf')] * n
        costs[0] = 0
        pq = [(0, 0)]
        while pq:
            distance, current = heapq.heappop(pq)
            if distance > costs[current]:
                continue
            for next_node, edge_cost in graph[current]:
                candidate = distance + edge_cost
                if candidate < costs[next_node]:
                    costs[next_node] = candidate
                    heapq.heappush(pq, (candidate, next_node))
        final = costs[n - 1]
        return final if final != float('inf') else -1
