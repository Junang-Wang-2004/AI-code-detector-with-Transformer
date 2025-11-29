class Solution:
    def minCost(self, n, edges, k):
        class DSU:
            def __init__(self, size):
                self.parent = list(range(size))
                self.sz = [1] * size

            def find(self, i):
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def merge(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                if pa == pb:
                    return False
                if self.sz[pa] < self.sz[pb]:
                    pa, pb = pb, pa
                self.parent[pb] = pa
                self.sz[pa] += self.sz[pb]
                return True

        sorted_edges = sorted(edges, key=lambda t: t[2])
        dsu = DSU(n)
        num_components = n
        for u, v, w in sorted_edges:
            if dsu.merge(u, v):
                num_components -= 1
                if num_components == k:
                    return w
        return 0
