class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.comps = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
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
        self.comps -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        dsu_alice = DSU(n)
        dsu_bob = DSU(n)
        to_remove = 0

        for edge in edges:
            if edge[0] == 3:
                conn_a = dsu_alice.unite(edge[1] - 1, edge[2] - 1)
                conn_b = dsu_bob.unite(edge[1] - 1, edge[2] - 1)
                if not conn_a and not conn_b:
                    to_remove += 1

        for edge in edges:
            if edge[0] == 1:
                if not dsu_alice.unite(edge[1] - 1, edge[2] - 1):
                    to_remove += 1

        for edge in edges:
            if edge[0] == 2:
                if not dsu_bob.unite(edge[1] - 1, edge[2] - 1):
                    to_remove += 1

        return to_remove if dsu_alice.comps == 1 and dsu_bob.comps == 1 else -1
