class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1
        self.comps = a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1, a2):
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
        self.comps -= 1
        return True

class C2:

    def maxNumEdgesToRemove(self, a1, a2):
        v1 = C1(a1)
        v2 = C1(a1)
        v3 = 0
        for v4 in a2:
            if v4[0] == 3:
                v5 = v1.unite(v4[1] - 1, v4[2] - 1)
                v6 = v2.unite(v4[1] - 1, v4[2] - 1)
                if not v5 and (not v6):
                    v3 += 1
        for v4 in a2:
            if v4[0] == 1:
                if not v1.unite(v4[1] - 1, v4[2] - 1):
                    v3 += 1
        for v4 in a2:
            if v4[0] == 2:
                if not v2.unite(v4[1] - 1, v4[2] - 1):
                    v3 += 1
        return v3 if v1.comps == 1 and v2.comps == 1 else -1
