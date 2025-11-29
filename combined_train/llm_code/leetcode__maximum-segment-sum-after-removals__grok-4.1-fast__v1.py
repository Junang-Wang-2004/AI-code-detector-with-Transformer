class C1:

    def __init__(self, a1):
        v1 = len(a1)
        self.parent = list(range(v1))
        self.rank = [0] * v1
        self.comp_sum = a1[:]

    def find(self, a1):
        v1 = a1
        while self.parent[v1] != v1:
            v1 = self.parent[v1]
        v2 = a1
        while v2 != v1:
            v3 = self.parent[v2]
            self.parent[v2] = v1
            v2 = v3
        return v1

    def unite(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
            self.comp_sum[v2] += self.comp_sum[v1]
        elif self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
            self.comp_sum[v1] += self.comp_sum[v2]
        else:
            self.parent[v2] = v1
            self.comp_sum[v1] += self.comp_sum[v2]
            self.rank[v1] += 1
        return True

    def get_sum(self, a1):
        return self.comp_sum[self.find(a1)]

class C2:

    def maximumSegmentSum(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = [False] * v1
        v4 = C1(a1)
        for v5 in range(1, v1):
            v6 = a2[v1 - v5]
            v3[v6] = True
            if v6 > 0 and v3[v6 - 1]:
                v4.unite(v6 - 1, v6)
            if v6 + 1 < v1 and v3[v6 + 1]:
                v4.unite(v6, v6 + 1)
            v2[v1 - v5 - 1] = max(v2[v1 - v5], v4.get_sum(v6))
        return v2
