class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.sz = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            self.parent[px] = py
            self.sz[py] += self.sz[px]
        else:
            self.parent[py] = px
            self.sz[px] += self.sz[py]
        return True


class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        q_with_idx = [q + [i] for i, q in enumerate(queries)]
        edgeList.sort(key=lambda e: e[2])
        q_with_idx.sort(key=lambda q: q[2])
        uf = UF(n)
        res = [False] * len(queries)
        j = 0
        for u, v, lim, i in q_with_idx:
            while j < len(edgeList) and edgeList[j][2] < lim:
                uf.unite(edgeList[j][0], edgeList[j][1])
                j += 1
            res[i] = uf.find(u) == uf.find(v)
        return res
