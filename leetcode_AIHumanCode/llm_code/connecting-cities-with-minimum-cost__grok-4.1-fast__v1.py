class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True


class Solution:
    def minimumCost(self, N, connections):
        edges = sorted(connections, key=lambda edge: edge[2])
        dsu = DSU(N)
        cost = 0
        for x, y, weight in edges:
            if dsu.merge(x - 1, y - 1):
                cost += weight
        return cost if dsu.components == 1 else -1
