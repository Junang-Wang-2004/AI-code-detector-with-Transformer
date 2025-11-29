class C1:

    def __init__(self, a1, a2):
        self.parent = list(range(a1 + 1))
        self.rank = [0] * (a1 + 1)
        self.comp_size = [1] * (a1 + 1)
        self.comp_size[a2] = 0
        self.top = a2

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
            self.comp_size[v2] += self.comp_size[v1]
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
            self.comp_size[v1] += self.comp_size[v2]
        else:
            self.parent[v2] = v1
            self.comp_size[v1] += self.comp_size[v2]
            self.rank[v1] += 1
        return True

    def size_top(self):
        return self.comp_size[self.find(self.top)]

class C2:

    def hitBricks(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 * v2
        v4 = v3
        v5 = [r[:] for v6 in a1]
        for v7, v8 in a2:
            v5[v7][v8] = 0
        v9 = C1(v3, v4)
        v10 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def idx(a1, a2):
            return a1 * v2 + a2
        for v11 in range(v1):
            for v12 in range(v2):
                if v5[v11][v12]:
                    v13 = idx(v11, v12)
                    if v11 == 0:
                        v9.unite(v13, v4)
                    if v11 > 0 and v5[v11 - 1][v12]:
                        v9.unite(v13, idx(v11 - 1, v12))
                    if v12 > 0 and v5[v11][v12 - 1]:
                        v9.unite(v13, idx(v11, v12 - 1))
        v14 = []
        for v7, v8 in reversed(a2):
            v15 = v9.size_top()
            if a1[v7][v8] == 0:
                v14.append(0)
                continue
            v5[v7][v8] = 1
            v13 = idx(v7, v8)
            if v7 == 0:
                v9.unite(v13, v4)
            for v16, v17 in v10:
                v18, v19 = (v7 + v16, v8 + v17)
                if 0 <= v18 < v1 and 0 <= v19 < v2 and v5[v18][v19]:
                    v9.unite(v13, idx(v18, v19))
            v20 = v9.size_top()
            v14.append(max(0, v20 - v15 - 1))
        return v14[::-1]
