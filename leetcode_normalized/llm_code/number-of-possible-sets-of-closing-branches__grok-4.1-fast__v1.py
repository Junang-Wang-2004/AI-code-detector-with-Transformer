class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        INF = float('inf')
        adj = [[INF] * n for _ in range(n)]
        for i in range(n):
            adj[i][i] = 0
        for u, v, w in roads:
            adj[u][v] = min(adj[u][v], w)
            adj[v][u] = min(adj[v][u], w)
        count = 0
        for state in range(1 << n):
            nodes = [i for i in range(n) if state & (1 << i)]
            size = len(nodes)
            if size == 0:
                count += 1
                continue
            matrix = [[INF] * size for _ in range(size)]
            for x in range(size):
                for y in range(size):
                    matrix[x][y] = adj[nodes[x]][nodes[y]]
            for k in range(size):
                for x in range(size):
                    for y in range
