class Solution:
    def criticalConnections(self, n, connections):
        self.graph = [[] for _ in range(n)]
        for a, b in connections:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.discover = [-1] * n
        self.lowest = [-1] * n
        self.counter = [0]
        self.crits = []
        self.dfs_traverse(0, -1)
        return self.crits

    def dfs_traverse(self, node, parent):
        self.discover[node] = self.lowest[node] = self.counter[0]
        self.counter[0] += 1
        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue
            if self.discover[neighbor] == -1:
                self.dfs_traverse(neighbor, node)
                self.lowest[node] = min(self.lowest[node], self.lowest[neighbor])
                if self.lowest[neighbor] > self.discover[node]:
                    self.crits.append([node, neighbor])
            elif neighbor != parent:
                self.lowest[node] = min(self.lowest[node], self.discover[neighbor])
