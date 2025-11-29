class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

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
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        indexed_edges = [list(e) + [i] for i, e in enumerate(edges)]
        indexed_edges.sort(key=lambda e: e[2])

        def mst_cost(skip_idx=-1, force_idx=-1):
            dsu = DSU(n)
            total_cost = 0
            if force_idx != -1:
                u, v, w, _ = indexed_edges[force_idx]
                if not dsu.merge(u, v):
                    return float('inf')
                total_cost += w
            for j in range(len(indexed_edges)):
                if j == skip_idx:
                    continue
                u, v, w, _ = indexed_edges[j]
                if dsu.merge(u, v):
                    total_cost += w
            return total_cost if dsu.components == 1 else float('inf')

        base_cost = mst_cost()
        critical = []
        pseudo_critical = []
        for idx in range(len(indexed_edges)):
            cost_skip = mst_cost(skip_idx=idx)
            if base_cost < cost_skip:
                critical.append(indexed_edges[idx][3])
            else:
                cost_force = mst_cost(force_idx=idx)
                if base_cost == cost_force:
                    pseudo_critical.append(indexed_edges[idx][3])
        return [critical, pseudo_critical]
