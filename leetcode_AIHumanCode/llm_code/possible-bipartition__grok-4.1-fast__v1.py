from collections import defaultdict

class Solution:
    def possibleBipartition(self, n, edges):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        assignment = [0] * n

        def explore(node, group):
            assignment[node] = group
            for adj_node in graph[node]:
                if assignment[adj_node] == 0:
                    if not explore(adj_node, 3 - group):
                        return False
                elif assignment[adj_node] == group:
                    return False
            return True

        for i in range(n):
            if assignment[i] == 0:
                if not explore(i, 1):
                    return False
        return True
