import heapq

class Solution:
    def findAnswer(self, n, edges):
        INF = float('inf')

        def shortest_distances(source):
            distances = [INF] * n
            distances[source] = 0
            pq = [(0, source)]
            while pq:
                distance, current = heapq.heappop(pq)
                if distance > distances[current]:
                    continue
                for neighbor, weight in graph[current]:
                    candidate = distance + weight
                    if candidate < distances[neighbor]:
                        distances[neighbor] = candidate
                        heapq.heappush(pq, (candidate, neighbor))
            return distances

        graph = [[] for _ in range(n)]
        for x, y, z in edges:
            graph[x].append((y, z))
            graph[y].append((x, z))

        dist_start = shortest_distances(0)
        dist_end = shortest_distances(n - 1)
        shortest = dist_start[n - 1]

        result = []
        for a, b, c in edges:
            if (dist_start[a] < INF and dist_end[b] < INF and
                dist_start[a] + c + dist_end[b] == shortest):
                result.append(True)
                continue
            if (dist_start[b] < INF and dist_end[a] < INF and
                dist_start[b] + c + dist_end[a] == shortest):
                result.append(True)
            else:
                result.append(False)
        return result
