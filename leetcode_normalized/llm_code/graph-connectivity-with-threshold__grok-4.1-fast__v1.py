class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1

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

    def merge(self, a1, a2):
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

    def areConnected(self, a1, a2, a3):
        v1 = C1(a1)
        for v2 in range(a2 + 1, a1 + 1):
            v3 = v2 * 2
            while v3 <= a1:
                v1.merge(v2 - 1, v3 - 1)
                v3 += v2
        v4 = []
        for v5 in a3:
            v6, v7 = v5
            v4.append(v1.find(v6 - 1) == v1.find(v7 - 1))
        return v4
