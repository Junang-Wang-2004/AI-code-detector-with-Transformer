from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs):
        graph = defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        start = next(node for node in graph if len(graph[node]) == 1)
        path = [start]
        previous = None
        current = start
        target_length = len(adjacentPairs) + 1
        while len(path) < target_length:
            for neighbor in graph[current]:
                if neighbor != previous:
                    path.append(neighbor)
                    previous = current
                    current = neighbor
                    break
        return path
