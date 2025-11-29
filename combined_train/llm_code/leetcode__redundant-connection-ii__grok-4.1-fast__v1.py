class C1:

    def __init__(self, a1):
        self.parent = list(range(a1 + 1))
        self.rank = [0] * (a1 + 1)

    def get(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.get(self.parent[a1])
        return self.parent[a1]

    def merge(self, a1, a2):
        v1 = self.get(a1)
        v2 = self.get(a2)
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

class C2:

    def findRedundantDirectedConnection(self, a1):
        v1 = len(a1)
        v2 = [-1] * (v1 + 1)
        v3 = v4 = None
        for v5, v6 in a1:
            if v2[v6] == -1:
                v2[v6] = v5
            else:
                v3 = [v2[v6], v6]
                v4 = [v5, v6]
        v7 = C1(v1)
        for v5, v6 in a1:
            if v4 and [v5, v6] == v4:
                continue
            if not v7.merge(v5, v6):
                return v3 if v4 else [v5, v6]
        return v4
