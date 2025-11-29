class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = float('inf')
        N = 26
        graph = [[INF] * N for _ in range(N)]
        for i in range(N):
            graph[i][i] = 0
        for j in range(len(original)):
            u = ord(original[j]) - ord('a')
            v = ord(changed[j]) - ord('a')
            graph[u][v] = min(graph[u][v], cost[j])
        for k in range(N):
            for x in range(N):
                for y in range(N):
                    graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])
        total = sum(graph[ord(source[p]) - ord('a')][ord(target[p]) - ord('a')] for p in range(len(source)))
        return total if total != INF else -1
