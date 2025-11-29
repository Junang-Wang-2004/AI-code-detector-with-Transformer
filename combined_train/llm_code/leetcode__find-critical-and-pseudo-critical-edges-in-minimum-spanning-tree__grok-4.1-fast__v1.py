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

    def findCriticalAndPseudoCriticalEdges(self, a1, a2):
        v1 = [list(e) + [i] for v2, v3 in enumerate(a2)]
        v1.sort(key=lambda e: v3[2])

        def mst_cost(a1=-1, a2=-1):
            v1 = C1(a1)
            v2 = 0
            if a2 != -1:
                v3, v4, v5, v6 = v1[a2]
                if not v1.merge(v3, v4):
                    return float('inf')
                v2 += v5
            for v7 in range(len(v1)):
                if v7 == a1:
                    continue
                v3, v4, v5, v6 = v1[v7]
                if v1.merge(v3, v4):
                    v2 += v5
            return v2 if v1.components == 1 else float('inf')
        v4 = mst_cost()
        v5 = []
        v6 = []
        for v7 in range(len(v1)):
            v8 = mst_cost(skip_idx=v7)
            if v4 < v8:
                v5.append(v1[v7][3])
            else:
                v9 = mst_cost(force_idx=v7)
                if v4 == v9:
                    v6.append(v1[v7][3])
        return [v5, v6]
