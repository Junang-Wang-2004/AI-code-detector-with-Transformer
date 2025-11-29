from collections import defaultdict, deque

class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        groups = 0
        for node in range(n):
            if node not in visited:
                groups += 1
                queue = deque([node])
                visited.add(node)
                while queue:
                    current = queue.popleft()
                    for neighbor in adj[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return groups - 1
