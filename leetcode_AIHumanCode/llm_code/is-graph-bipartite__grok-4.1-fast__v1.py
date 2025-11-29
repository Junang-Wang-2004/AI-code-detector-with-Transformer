from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        colors = [-1] * n
        for start in range(n):
            if colors[start] != -1:
                continue
            queue = deque([start])
            colors[start] = 0
            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if colors[adj] == -1:
                        colors[adj] = 1 - colors[node]
                        queue.append(adj)
                    elif colors[adj] == colors[node]:
                        return False
        return True
