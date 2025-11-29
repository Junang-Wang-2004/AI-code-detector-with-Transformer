class C1:

    def minCost(self, a1, a2, a3):

        class DSU:

            def __init__(self, a1):
                self.parent = list(range(a1))
                self.sz = [1] * a1

            def find(self, a1):
                if self.parent[a1] != a1:
                    self.parent[a1] = self.find(self.parent[a1])
                return self.parent[a1]

            def merge(self, a1, a2):
                v1 = self.find(a1)
                v2 = self.find(a2)
                if v1 == v2:
                    return False
                if self.sz[v1] < self.sz[v2]:
                    v1, v2 = (v2, v1)
                self.parent[v2] = v1
                self.sz[v1] += self.sz[v2]
                return True
        v1 = sorted(a2, key=lambda t: t[2])
        v2 = DSU(a1)
        v3 = a1
        for v4, v5, v6 in v1:
            if v2.merge(v4, v5):
                v3 -= 1
                if v3 == a3:
                    return v6
        return 0
