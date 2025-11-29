class UnionFind:
    def __init__(self, n, values):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.node_counts = [{} for _ in range(n)]
        for i, v in enumerate(values):
            self.node_counts[i][v] = 1

    def get_root(self, i):
        r = i
        while self.parents[r] != r:
            r = self.parents[r]
        j = i
        while j != r:
            nxt = self.parents[j]
            self.parents[j] = r
            j = nxt
        return r

    def link(self, i, j, val):
        ri = self.get_root(i)
        rj = self.get_root(j)
        if ri == rj:
            return 0
        if self.ranks[ri] > self.ranks[rj]:
            ri, rj = rj, ri
        self.parents[ri] = rj
        if self.ranks[ri] == self.ranks[rj]:
            self.ranks[rj] += 1
        ci = self.node_counts[ri].get(val, 0)
        cj = self.node_counts[rj].get(val, 0)
        self.node_counts[rj][val] = ci + cj
        return ci * cj


class Solution:
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)
        sorted_edges = sorted(edges, key=lambda p: max(vals[p[0]], vals[p[1]]))
        uf = UnionFind(n, vals)
        result = n
        for u, v in sorted_edges:
            mx = max(vals[u], vals[v])
            result += uf.link(u, v, mx)
        return result
