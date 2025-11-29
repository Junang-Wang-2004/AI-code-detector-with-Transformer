class Solution(object):
    def maxStarSum(self, vals, edges, k):
        n = len(vals)
        graph = [[] for _ in range(n)]
        for x, y in edges:
            if vals[y] > 0:
                graph[x].append(y)
            if vals[x] > 0:
                graph[y].append(x)
        best = float('-inf')
        for node in range(n):
            nbr_vals = sorted(vals[v] for v in graph[node], reverse=True)
            total = vals[node] + sum(nbr_vals[:k])
            if total > best:
                best = total
        return best
