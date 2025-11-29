class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1
        self.groups = a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1, a2):
        v1, v2 = (self.find(a1), self.find(a2))
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1
        self.groups -= 1
        return True

class C2:

    def earliestAcq(self, a1, a2):
        a1.sort(key=lambda x: x[0])
        v1 = C1(a2)
        for v2, v3, v4 in a1:
            v1.unite(v3, v4)
            if v1.groups == 1:
                return v2
        return -1
