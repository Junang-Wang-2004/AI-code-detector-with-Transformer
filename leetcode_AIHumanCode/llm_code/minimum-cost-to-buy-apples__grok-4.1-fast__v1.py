import heapq

class Solution(object):
    def minCost(self, n, roads, appleCost, k):
        multiplier = k + 1
        INF = 10**20
        graph = [[] for _ in range(n + 1)]
        for x, y, toll in roads:
            u = x - 1
            v = y - 1
            edge_weight = toll * multiplier
            graph[u].append((v, edge_weight))
            graph[v].append((u, edge_weight))
        source = n
        for i in range(n):
            graph[source].append((i, appleCost[i]))
        distances = [INF] * (n + 1)
        distances[source] = 0
        priority_queue = [(0, source)]
        while priority_queue:
            current_cost, node = heapq.heappop(priority_queue)
            if current_cost > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                new_cost = current_cost + weight
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
        return distances[:n]
