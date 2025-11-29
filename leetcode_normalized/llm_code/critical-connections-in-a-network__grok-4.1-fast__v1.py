class C1:

    def criticalConnections(self, a1, a2):
        self.graph = [[] for v1 in range(a1)]
        for v2, v3 in a2:
            self.graph[v2].append(v3)
            self.graph[v3].append(v2)
        self.discover = [-1] * a1
        self.lowest = [-1] * a1
        self.counter = [0]
        self.crits = []
        self.dfs_traverse(0, -1)
        return self.crits

    def dfs_traverse(self, a1, a2):
        self.discover[a1] = self.lowest[a1] = self.counter[0]
        self.counter[0] += 1
        for v1 in self.graph[a1]:
            if v1 == a2:
                continue
            if self.discover[v1] == -1:
                self.dfs_traverse(v1, a1)
                self.lowest[a1] = min(self.lowest[a1], self.lowest[v1])
                if self.lowest[v1] > self.discover[a1]:
                    self.crits.append([a1, v1])
            elif v1 != a2:
                self.lowest[a1] = min(self.lowest[a1], self.discover[v1])
