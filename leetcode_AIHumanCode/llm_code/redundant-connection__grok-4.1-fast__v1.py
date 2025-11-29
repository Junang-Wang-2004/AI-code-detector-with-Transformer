class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def get_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get_root(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        rx, ry = self.get_root(x), self.get_root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


class Solution:
    def findRedundantConnection(self, pairs):
        finder = DSU(len(pairs) + 1)
        for u, v in pairs:
            if not finder.merge(u, v):
                return [u, v]
        return []
