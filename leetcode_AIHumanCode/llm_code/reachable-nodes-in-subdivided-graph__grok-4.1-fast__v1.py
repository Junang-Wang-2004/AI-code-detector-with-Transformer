import heapq

class Solution(object):
    def reachableNodes(self, edges, M, N):
        graph = [[] for _ in range(N)]
        for x, y, z in edges:
            graph[x].append((y, z))
            graph[y].append((x, z))
        distance = [float('inf')] * N
        distance[0] = 0
        priority_queue = []
        heapq.heappush(priority_queue, (0, 0))
        while priority_queue:
            path_cost, current = heapq.heappop(priority_queue)
            if path_cost > distance[current]:
                continue
            for neighbor, edge_cost in graph[current]:
                candidate = path_cost + edge_cost + 1
                if candidate <= M and candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heapq.heappush(priority_queue, (candidate, neighbor))
        total = sum(1 for d in distance if d <= M)
        for x, y, z in edges:
            left_x = max(0, M - distance[x]) if distance[x] <= M else 0
            left_y = max(0, M - distance[y]) if distance[y] <= M else 0
            total += min(z, left_x + left_y)
        return total
