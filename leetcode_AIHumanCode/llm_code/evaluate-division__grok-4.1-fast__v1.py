class UnionFind:
    def __init__(self):
        self.par = {}
        self.mul = {}
        self.rnk = {}

    def get(self, x):
        if x not in self.par:
            self.par[x] = x
            self.mul[x] = 1.0
            self.rnk[x] = 0
            return x
        if self.par[x] != x:
            p = self.par[x]
            self.par[x] = self.get(p)
            self.mul[x] *= self.mul[p]
        return self.par[x]

    def merge(self, x, y, k):
        rx = self.get(x)
        ry = self.get(y)
        if rx == ry:
            return False
        mx = self.mul[x]
        my = self.mul[y]
        if self.rnk[rx] < self.rnk[ry]:
            self.par[rx] = ry
            self.mul[rx] = k * my / mx
        elif self.rnk[rx] > self.rnk[ry]:
            self.par[ry] = rx
            self.mul[ry] = mx / (k * my)
        else:
            self.par[ry] = rx
            self.mul[ry] = mx / (k * my)
            self.rnk[rx] += 1
        return True

    def get_ratio(self, x, y):
        if x not in self.par or y not in self.par:
            return -1.0
        rx = self.get(x)
        ry = self.get(y)
        if rx != ry:
            return -1.0
        return self.mul[x] / self.mul[y]


class Solution:
    def calcEquation(self, equations, values, queries):
        uf = UnionFind()
        for eq, val in zip(equations, values):
            uf.merge(eq[0], eq[1], val)
        return [uf.get_ratio(q[0], q[1]) for q in queries]
