class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        edges = [[] for _ in range(n)]
        for i in range(n - 1):
            edges[i].append(i + 1)
        res = []
        INF = float('inf')
        for a, b in queries:
            edges[a].append(b)
            costs = [INF] * n
            costs[0] = 0
            for i in range(n):
                for j in edges[i]:
                    costs[j] = min(costs[j], costs[i] + 1)
            res.append(costs[n - 1])
        return res
