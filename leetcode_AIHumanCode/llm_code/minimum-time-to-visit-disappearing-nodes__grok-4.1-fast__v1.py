import heapq

class Solution:
    def minimumTime(self, n, edges, disappear):
        INF = float('inf')
        graph = [[] for _ in range(n)]
        for a, b, t in edges:
            graph[a].append((b, t))
            graph[b].append((a, t))
        distance = [INF] * n
        distance[0] = 0
        priority_queue = [(0, 0)]
        while priority_queue:
            current_time, current_node = heapq.heappop(priority_queue)
            if current_time > distance[current_node]:
                continue
            for next_node, travel_time in graph[current_node]:
                arrival_time = current_time + travel_time
                if arrival_time < distance[next_node] and arrival_time < disappear[next_node]:
                    distance[next_node] = arrival_time
                    heapq.heappush(priority_queue, (arrival_time, next_node))
        return [-1 if d == INF else int(d) for d in distance]
