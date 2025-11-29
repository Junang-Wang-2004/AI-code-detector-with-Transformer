class C1:

    def __init__(self, a1):
        self.size = a1
        self.data = [0] * (a1 + 1)

    def modify(self, a1, a2):
        while a1 <= self.size:
            self.data[a1] += a2
            a1 += a1 & -a1

    def prefix_sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.data[a1]
            a1 -= a1 & -a1
        return v1

class C2:

    def processQueries(self, a1, a2):
        v1 = C1(2 * a2 + 1)
        v2 = [0] * (a2 + 1)
        v3 = a2
        v4 = []
        for v5 in range(1, a2 + 1):
            v6 = a2 + v5
            v2[v5] = v6
            v1.modify(v6, 1)
        for v7 in a1:
            v8 = v2[v7]
            v4.append(v1.prefix_sum(v8 - 1))
            v1.modify(v8, -1)
            v2[v7] = v3
            v1.modify(v3, 1)
            v3 -= 1
        return v4
