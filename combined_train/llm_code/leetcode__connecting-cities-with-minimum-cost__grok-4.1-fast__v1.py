class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1
        self.components = a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def merge(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1
        self.components -= 1
        return True

class C2:

    def minimumCost(self, a1, a2):
        v1 = sorted(a2, key=lambda edge: edge[2])
        v2 = C1(a1)
        v3 = 0
        for v4, v5, v6 in v1:
            if v2.merge(v4 - 1, v5 - 1):
                v3 += v6
        return v3 if v2.components == 1 else -1
