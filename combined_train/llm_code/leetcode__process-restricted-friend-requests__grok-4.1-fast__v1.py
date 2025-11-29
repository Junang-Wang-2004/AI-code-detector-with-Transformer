class C1:

    def __init__(self, a1):
        self.p = list(range(a1))
        self.rank = [0] * a1

    def find(self, a1):
        if self.p[a1] != a1:
            self.p[a1] = self.find(self.p[a1])
        return self.p[a1]

    def unite(self, a1, a2):
        v1 = self.find(a1)
        v2 = self.find(a2)
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.p[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.p[v2] = v1
        else:
            self.p[v2] = v1
            self.rank[v1] += 1
        return True

class C2:

    def friendRequests(self, a1, a2, a3):
        v1 = C1(a1)
        v2 = []
        for v3, v4 in a3:
            v5 = v1.find(v3)
            v6 = v1.find(v4)
            if v5 == v6:
                v2.append(True)
                continue
            v7 = True
            for v8, v9 in a2:
                v10 = v1.find(v8)
                v11 = v1.find(v9)
                if v10 == v5 and v11 == v6 or (v10 == v6 and v11 == v5):
                    v7 = False
                    break
            v2.append(v7)
            if v7:
                v1.unite(v3, v4)
        return v2
