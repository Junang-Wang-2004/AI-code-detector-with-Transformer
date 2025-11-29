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

    def findAllPeople(self, a1, a2, a3):
        a2.sort(key=lambda t: t[2])
        v1 = {0, a3}
        v2 = 0
        v3 = len(a2)
        while v2 < v3:
            v4 = a2[v2][2]
            v5 = []
            v6 = set()
            while v2 < v3 and a2[v2][2] == v4:
                v7, v8, v9 = a2[v2]
                v5.append((v7, v8))
                v6.add(v7)
                v6.add(v8)
                v2 += 1
            if not v6:
                continue
            v10 = C1(a1)
            for v7, v8 in v5:
                v10.unite(v7, v8)
            v11 = {v10.find(p) for v12 in v6 if v12 in v1}
            for v12 in v6:
                if v10.find(v12) in v11:
                    v1.add(v12)
        return sorted(v1)
