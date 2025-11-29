class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))
        self.rank = [0] * a1
        self.components = a1

    def find(self, a1):
        if self.parent[a1] != a1:
            self.parent[a1] = self.find(self.parent[a1])
        return self.parent[a1]

    def link(self, a1, a2):
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
        self.components -= 1

class C2:

    def regionsBySlashes(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = C1(4 * v1 * v2)

        def get_id(a1, a2, a3):
            return a1 * (4 * v2) + a2 * 4 + a3
        v4, v5, v6, v7 = (0, 1, 2, 3)
        for v8 in range(1, v1):
            for v9 in range(v2):
                v3.link(get_id(v8 - 1, v9, v6), get_id(v8, v9, v4))
        for v8 in range(v1):
            for v9 in range(1, v2):
                v3.link(get_id(v8, v9 - 1, v5), get_id(v8, v9, v7))
        for v8 in range(v1):
            for v9 in range(v2):
                v10 = a1[v8][v9]
                if v10 != '/':
                    v3.link(get_id(v8, v9, v4), get_id(v8, v9, v5))
                    v3.link(get_id(v8, v9, v6), get_id(v8, v9, v7))
                if v10 != '\\':
                    v3.link(get_id(v8, v9, v7), get_id(v8, v9, v4))
                    v3.link(get_id(v8, v9, v5), get_id(v8, v9, v6))
        return v3.components
