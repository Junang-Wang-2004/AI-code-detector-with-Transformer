class Solution:
    def maximumImportance(self, n, roads):
        node_degrees = [0] * n
        for u, v in roads:
            node_degrees[u] += 1
            node_degrees[v] += 1
        node_degrees.sort(reverse=True)
        total = 0
        for i in range(n):
            total += node_degrees[i] * (n - i)
        return total
