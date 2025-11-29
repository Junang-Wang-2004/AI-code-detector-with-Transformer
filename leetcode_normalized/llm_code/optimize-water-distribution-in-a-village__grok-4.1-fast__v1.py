class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1
        self.components = a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def merge(self, a1, a2):
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
        self.components -= 1
        return True

class C2:

    def minCostToSupplyWater(self, a1, a2, a3):
        v1 = C1(a1 + 1)
        v2 = []
        for v3 in range(1, a1 + 1):
            v2.append((a2[v3 - 1], 0, v3))
        for v4, v5, v6 in a3:
            v2.append((v6, v4, v5))
        v2.sort()
        v7 = 0
        for v6, v8, v9 in v2:
            if v1.merge(v8, v9):
                v7 += v6
                if v1.components == 1:
                    return v7
        return v7
