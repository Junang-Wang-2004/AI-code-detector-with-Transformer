class C1:

    def __init__(self, a1):
        self.par = list(range(a1))
        self.rnk = [0] * a1
        self.mx = list(range(a1))

    def root(self, a1):
        if self.par[a1] != a1:
            self.par[a1] = self.root(self.par[a1])
        return self.par[a1]

    def merge(self, a1, a2):
        v1 = self.root(a1)
        v2 = self.root(a2)
        if v1 == v2:
            return
        if self.rnk[v1] < self.rnk[v2]:
            self.par[v1] = v2
            self.mx[v2] = max(self.mx[v1], self.mx[v2])
        else:
            self.par[v2] = v1
            self.mx[v1] = max(self.mx[v2], self.mx[v1])
            if self.rnk[v1] == self.rnk[v2]:
                self.rnk[v1] += 1

    def max_in(self, a1):
        return self.mx[self.root(a1)]

class C2:

    def minReverseOperations(self, a1, a2, a3, a4):
        v1 = [False] * a1
        for v2 in a3:
            v1[v2] = True
        v3 = [-1] * a1
        v3[a2] = 0
        v4 = C1(a1 + 2)
        v4.merge(a2, a2 + 2)
        v5 = [a2]
        v6 = 1
        while v5:
            v7 = []
            for v8 in v5:
                v9 = max(0, v8 - a4 + 1)
                v10 = min(v8, a1 - a4)
                v11 = 2 * v9 + a4 - 1 - v8
                v12 = 2 * v10 + a4 - 1 - v8
                v2 = v4.max_in(v11)
                while v2 <= v12:
                    if not v1[v2]:
                        v3[v2] = v6
                        v7.append(v2)
                    v4.merge(v2, v2 + 2)
                    v2 = v4.max_in(v2)
            v5 = v7
            v6 += 1
        return v3
