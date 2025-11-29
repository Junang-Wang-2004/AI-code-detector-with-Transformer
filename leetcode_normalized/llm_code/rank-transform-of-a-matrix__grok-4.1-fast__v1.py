import collections

class C1(object):

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
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1
        return True

class C2(object):

    def matrixRankTransform(self, a1):
        if not a1 or not a1[0]:
            return a1
        v1, v2 = (len(a1), len(a1[0]))
        v3 = collections.defaultdict(list)
        for v4 in range(v1):
            for v5 in range(v2):
                v3[a1[v4][v5]].append((v4, v5))
        v6 = [0] * v1
        v7 = [0] * v2
        for v8 in sorted(v3):
            v9 = v3[v8]
            v10 = C1(v1 + v2)
            for v4, v5 in v9:
                v10.unite(v4, v1 + v5)
            v11 = {}
            for v4, v5 in v9:
                v12 = v10.find(v4)
                v11[v12] = max(v11.get(v12, 0), v6[v4])
                v13 = v10.find(v1 + v5)
                v11[v13] = max(v11.get(v13, 0), v7[v5])
            for v4, v5 in v9:
                v14 = v10.find(v4)
                v15 = v11[v14] + 1
                a1[v4][v5] = v15
                v6[v4] = v15
                v7[v5] = v15
        return a1
