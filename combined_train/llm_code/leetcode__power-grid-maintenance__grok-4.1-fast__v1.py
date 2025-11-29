class C1(object):

    def processQueries(self, a1, a2, a3):

        class UnionFind:

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
        v1 = UnionFind(a1)
        for v2, v3 in a2:
            v1.unite(v2 - 1, v3 - 1)
        v4 = {}
        for v5 in range(a1 - 1, -1, -1):
            v6 = v1.find(v5)
            if v6 not in v4:
                v4[v6] = []
            v4[v6].append(v5)
        v7 = [True] * a1
        v8 = []
        for v9, v10 in a3:
            v11 = v10 - 1
            if v9 == 2:
                v7[v11] = False
            else:
                v6 = v1.find(v11)
                v12 = v4[v6]
                if v7[v11]:
                    v8.append(v11 + 1)
                else:
                    while v12 and (not v7[v12[-1]]):
                        v12.pop()
                    v8.append(v12[-1] + 1 if v12 else -1)
        return v8
