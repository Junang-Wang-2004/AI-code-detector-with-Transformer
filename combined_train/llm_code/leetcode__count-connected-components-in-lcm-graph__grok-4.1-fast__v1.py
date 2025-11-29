class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1, a2):
        v1, v2 = (self.find(a1), self.find(a2))
        if v1 == v2:
            return
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1

class C2:

    def countComponents(self, a1, a2):
        v1 = C1(a2)
        v2 = sum((1 for v3 in a1 if v3 > a2))
        v4 = set()
        for v3 in a1:
            if v3 > a2:
                continue
            v5 = v3 - 1
            v6 = v3 * 2
            while v6 <= a2:
                v1.unite(v5, v6 - 1)
                v6 += v3
            v4.add(v1.find(v5))
        return v2 + len(v4)
