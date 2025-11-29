import heapq

class Solution:
    def minimumCost(self, n, highways, discounts):
        graph = [[] for _ in range(n)]
        for a, b, cost in highways:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        INF = float('inf')
        distances = [[INF] * (discounts + 1) for _ in range(n)]
        distances[0][discounts] = 0
        pq = [(0, 0, discounts)]
        end = n - 1
        while pq:
            total, curr, left = heapq.heappop(pq)
            if total > distances[curr][left]:
                continue
            if curr == end:
                return total
            for next_node, edge_cost in graph[curr]:
                updated = total + edge_cost
                if updated < distances[next_node][left]:
                    distances[next_node][left] = updated
                    heapq.heappush(pq, (updated, next_node, left))
                if left > 0:
                    halved = total + (edge_cost // 2)
                    if halved < distances[next_node][left - 1]:
                        distances[next_node][left - 1] = halved
                        heapq.heappush(pq, (halved, next_node, left - 1))
        return -1
