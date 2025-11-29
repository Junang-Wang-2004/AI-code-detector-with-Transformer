class Solution:
    def findTheCity(self, num_cities, connections, max_dist):
        graph = [[float('inf')] * num_cities for _ in range(num_cities)]
        for u, v, weight in connections:
            graph[u][v] = graph[v][u] = weight
        for i in range(num_cities):
            graph[i][i] = 0
        for k in range(num_cities):
            for i in range(num_cities):
                for j in range(num_cities):
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        min_count = float('inf')
        best_city = -1
        for city in range(num_cities):
            nearby = sum(1 for d in graph[city] if d <= max_dist)
            if nearby < min_count:
                min_count = nearby
                best_city = city
            elif nearby == min_count:
                best_city = city
        return best_city
