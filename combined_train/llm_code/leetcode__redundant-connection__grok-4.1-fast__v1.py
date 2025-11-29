class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1

    def get_root(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.get_root(self.parent[a1])
        return self.parent[a1]

    def merge(self, a1, a2):
        v1, v2 = (self.get_root(a1), self.get_root(a2))
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

    def findRedundantConnection(self, a1):
        v1 = C1(len(a1) + 1)
        for v2, v3 in a1:
            if not v1.merge(v2, v3):
                return [v2, v3]
        return []
