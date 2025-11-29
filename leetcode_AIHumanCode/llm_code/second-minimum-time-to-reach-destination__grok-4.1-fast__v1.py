from collections import deque

class Solution:
    def secondMinimum(self, n, edges, time, change):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

        def shortest_distances(src):
            distances = [-1] * n
            distances[src] = 0
            queue = deque([src])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)
            return distances

        from_start = shortest_distances(0)
        shortest = from_start[n - 1]
        from_goal = shortest_distances(n - 1)

        min_longer = shortest + 2
        for node in range(n):
            path_len = from_start[node] + from_goal[node]
            if path_len > shortest:
                min_longer = min(min_longer, path_len)

        current = 0
        for _ in range(min_longer):
            if (current // change) % 2 == 1:
                current = ((current // change) + 1) * change
            current += time
        return current
