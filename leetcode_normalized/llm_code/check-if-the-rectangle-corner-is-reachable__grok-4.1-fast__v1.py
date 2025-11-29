class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def unite(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
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

    def canReachCorner(self, a1, a2, a3):
        v1 = len(a3)
        if v1 == 0:
            return True
        v2 = C1(v1 + 2)
        v3 = v1
        v4 = v1 + 1
        for v5 in range(v1):
            v6, v7, v8 = a3[v5]
            if v6 - v8 <= 0 or v7 + v8 >= a2:
                v2.unite(v5, v3)
            if v6 + v8 >= a1 or v7 - v8 <= 0:
                v2.unite(v5, v4)
        for v5 in range(v1):
            v9, v10, v11 = a3[v5]
            for v12 in range(v5):
                v13, v14, v15 = a3[v12]
                v16 = v9 - v13
                v17 = v10 - v14
                if v16 * v16 + v17 * v17 <= (v11 + v15) * (v11 + v15):
                    v2.unite(v5, v12)
        return v2.find(v3) != v2.find(v4)
