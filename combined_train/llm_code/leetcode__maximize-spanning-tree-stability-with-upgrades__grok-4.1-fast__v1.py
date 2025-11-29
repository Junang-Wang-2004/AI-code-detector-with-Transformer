class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.size = [1] * a1

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
        if self.size[v1] < self.size[v2]:
            v1, v2 = (v2, v1)
        self.parent[v2] = v1
        self.size[v1] += self.size[v2]
        return True

class C2:

    def maxStability(self, a1, a2, a3):
        v1 = C1(a1)
        v2 = float('inf')
        v3 = 0
        for v4, v5, v6, v7 in a2:
            if not v7:
                continue
            if not v1.unite(v4, v5):
                return -1
            v2 = min(v2, v6)
            v3 += 1
        v8 = [(v6, v4, v5) for v4, v5, v6, v7 in a2 if not v7]
        v8.sort(reverse=True)
        v9 = a1 - 1
        v10 = v2
        for v6, v4, v5 in v8:
            if v1.unite(v4, v5):
                v3 += 1
                if v3 == v9 - a3:
                    v10 = min(v10, v6)
                elif v3 == v9:
                    v10 = min(v10, 2 * v6)
        return v10 if v3 == v9 else -1
