class C1:

    def __init__(self, a1, a2):
        self.parents = list(range(a1))
        self.ranks = [0] * a1
        self.node_counts = [{} for v1 in range(a1)]
        for v2, v3 in enumerate(a2):
            self.node_counts[v2][v3] = 1

    def get_root(self, a1):
        v1 = a1
        while self.parents[v1] != v1:
            v1 = self.parents[v1]
        v2 = a1
        while v2 != v1:
            v3 = self.parents[v2]
            self.parents[v2] = v1
            v2 = v3
        return v1

    def link(self, a1, a2, a3):
        v1 = self.get_root(a1)
        v2 = self.get_root(a2)
        if v1 == v2:
            return 0
        if self.ranks[v1] > self.ranks[v2]:
            v1, v2 = (v2, v1)
        self.parents[v1] = v2
        if self.ranks[v1] == self.ranks[v2]:
            self.ranks[v2] += 1
        v3 = self.node_counts[v1].get(a3, 0)
        v4 = self.node_counts[v2].get(a3, 0)
        self.node_counts[v2][a3] = v3 + v4
        return v3 * v4

class C2:

    def numberOfGoodPaths(self, a1, a2):
        v1 = len(a1)
        v2 = sorted(a2, key=lambda p: max(a1[p[0]], a1[p[1]]))
        v3 = C1(v1, a1)
        v4 = v1
        for v5, v6 in v2:
            v7 = max(a1[v5], a1[v6])
            v4 += v3.link(v5, v6, v7)
        return v4
