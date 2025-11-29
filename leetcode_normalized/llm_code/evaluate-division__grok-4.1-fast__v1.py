class C1:

    def __init__(self):
        self.par = {}
        self.mul = {}
        self.rnk = {}

    def get(self, a1):
        if a1 not in self.par:
            self.par[a1] = a1
            self.mul[a1] = 1.0
            self.rnk[a1] = 0
            return a1
        if self.par[a1] != a1:
            v1 = self.par[a1]
            self.par[a1] = self.get(v1)
            self.mul[a1] *= self.mul[v1]
        return self.par[a1]

    def merge(self, a1, a2, a3):
        v1 = self.get(a1)
        v2 = self.get(a2)
        if v1 == v2:
            return False
        v3 = self.mul[a1]
        v4 = self.mul[a2]
        if self.rnk[v1] < self.rnk[v2]:
            self.par[v1] = v2
            self.mul[v1] = a3 * v4 / v3
        elif self.rnk[v1] > self.rnk[v2]:
            self.par[v2] = v1
            self.mul[v2] = v3 / (a3 * v4)
        else:
            self.par[v2] = v1
            self.mul[v2] = v3 / (a3 * v4)
            self.rnk[v1] += 1
        return True

    def get_ratio(self, a1, a2):
        if a1 not in self.par or a2 not in self.par:
            return -1.0
        v1 = self.get(a1)
        v2 = self.get(a2)
        if v1 != v2:
            return -1.0
        return self.mul[a1] / self.mul[a2]

class C2:

    def calcEquation(self, a1, a2, a3):
        v1 = C1()
        for v2, v3 in zip(a1, a2):
            v1.merge(v2[0], v2[1], v3)
        return [v1.get_ratio(q[0], q[1]) for v4 in a3]
