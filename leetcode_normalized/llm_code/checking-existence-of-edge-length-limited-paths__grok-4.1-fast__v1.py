class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.sz = [1] * a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.sz[v1] < self.sz[v2]:
            self.parent[v1] = v2
            self.sz[v2] += self.sz[v1]
        else:
            self.parent[v2] = v1
            self.sz[v1] += self.sz[v2]
        return True

class C2:

    def distanceLimitedPathsExist(self, a1, a2, a3):
        v1 = [q + [i] for v2, v3 in enumerate(a3)]
        a2.sort(key=lambda e: e[2])
        v1.sort(key=lambda q: v3[2])
        v4 = C1(a1)
        v5 = [False] * len(a3)
        v6 = 0
        for v7, v8, v9, v2 in v1:
            while v6 < len(a2) and a2[v6][2] < v9:
                v4.unite(a2[v6][0], a2[v6][1])
                v6 += 1
            v5[v2] = v4.find(v7) == v4.find(v8)
        return v5
