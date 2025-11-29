class C1:

    def countPaths(self, a1, a2):
        v1 = [True] * (a1 + 1)
        v1[0] = v1[1] = False
        for v2 in range(2, int(a1 ** 0.5) + 1):
            if v1[v2]:
                for v3 in range(v2 * v2, a1 + 1, v2):
                    v1[v3] = False

        class UF:

            def __init__(self, a1):
                self.parent = list(range(a1))
                self.csize = [1] * a1

            def find(self, a1):
                if self.parent[a1] != a1:
                    self.parent[a1] = self.find(self.parent[a1])
                return self.parent[a1]

            def merge(self, a1, a2):
                v1, v2 = (self.find(a1), self.find(a2))
                if v1 == v2:
                    return
                if self.csize[v1] < self.csize[v2]:
                    v1, v2 = (v2, v1)
                self.parent[v2] = v1
                self.csize[v1] += self.csize[v2]

            def csize_of(self, a1):
                return self.csize[self.find(a1)]
        v4 = UF(a1)
        for v5, v6 in a2:
            v7, v8 = (v5 - 1, v6 - 1)
            if not v1[v7 + 1] and (not v1[v8 + 1]):
                v4.merge(v7, v8)
        v9 = [1] * a1
        v10 = 0
        for v5, v6 in a2:
            v7, v8 = (v5 - 1, v6 - 1)
            if v1[v7 + 1] == v1[v8 + 1]:
                continue
            if not v1[v7 + 1]:
                v7, v8 = (v8, v7)
            v11 = v4.csize_of(v8)
            v10 += v9[v7] * v11
            v9[v7] += v11
        return v10
