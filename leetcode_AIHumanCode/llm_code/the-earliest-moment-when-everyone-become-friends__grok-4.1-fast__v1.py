class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.groups = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.groups -= 1
        return True


class Solution:
    def earliestAcq(self, logs, N):
        logs.sort(key=lambda x: x[0])
        dsu = DSU(N)
        for time, x, y in logs:
            dsu.unite(x, y)
            if dsu.groups == 1:
                return time
        return -1
