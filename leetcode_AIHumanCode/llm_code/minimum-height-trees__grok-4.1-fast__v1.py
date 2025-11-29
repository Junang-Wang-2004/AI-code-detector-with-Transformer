from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [0] if n == 1 else []
        
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        queue = deque(i for i in range(n) if degree[i] <= 1)
        remaining = n
        while remaining > 2:
            layer_size = len(queue)
            remaining -= layer_size
            for _ in range(layer_size):
                node = queue.popleft()
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)
        
        return list(queue)
