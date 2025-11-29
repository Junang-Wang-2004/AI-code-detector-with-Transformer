class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        return root

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        return True


class Solution:
    def minTime(self, n, edges, k):
        edges.sort(key=lambda e: -e[2])
        uf = UnionFind(n)
        components = n
        for a, b, tm in edges:
            if uf.find(a) != uf.find(b):
                if components == k:
                    return tm
                uf.unite(a, b)
                components -= 1
        return 0
