import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        if n < 2:
            return 0
        visited = [False] * n
        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        total_cost = 0
        while min_heap:
            edge_weight, node_idx = heapq.heappop(min_heap)
            if visited[node_idx]:
                continue
            visited[node_idx] = True
            total_cost += edge_weight
            px, py = points[node_idx]
            for next_idx in range(n):
                if not visited[next_idx]:
                    qx, qy = points[next_idx]
                    distance = abs(px - qx) + abs(py - qy)
                    heapq.heappush(min_heap, (distance, next_idx))
        return total_cost
