class DSU:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)

    def get(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.get(self.parent[i])
        return self.parent[i]

    def merge(self, a, b):
        ra = self.get(a)
        rb = self.get(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        prev_in = [-1] * (n + 1)
        first_cand = second_cand = None
        for a, b in edges:
            if prev_in[b] == -1:
                prev_in[b] = a
            else:
                first_cand = [prev_in[b], b]
                second_cand = [a, b]
        uf = DSU(n)
        for a, b in edges:
            if second_cand and [a, b] == second_cand:
                continue
            if not uf.merge(a, b):
                return first_cand if second_cand else [a, b]
        return second_cand
