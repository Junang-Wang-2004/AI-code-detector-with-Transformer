class C1:

    def countOfPeaks(self, a1, a2):
        v1 = len(a1)

        class Fenwick:

            def __init__(self, a1):
                self.size = a1
                self.tree = [0] * (a1 + 1)

            def update(self, a1, a2):
                a1 += 1
                while a1 <= self.size:
                    self.tree[a1] += a2
                    a1 += a1 & -a1

            def prefix(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 += self.tree[a1]
                    a1 -= a1 & -a1
                return v2
        v2 = Fenwick(v1)
        for v3 in range(1, v1 - 1):
            if a1[v3 - 1] < a1[v3] > a1[v3 + 1]:
                v2.update(v3, 1)
        v4 = []
        for v5 in a2:
            v6, v7, v8 = v5
            if v6 == 1:
                if v8 - 1 < v7 + 1:
                    v4.append(0)
                else:
                    v4.append(v2.prefix(v8 - 1) - v2.prefix(v7))
            else:
                v9 = range(max(v7 - 1, 1), min(v7 + 2, v1 - 1))
                for v10 in v9:
                    if a1[v10 - 1] < a1[v10] > a1[v10 + 1]:
                        v2.update(v10, -1)
                a1[v7] = v8
                for v10 in v9:
                    if a1[v10 - 1] < a1[v10] > a1[v10 + 1]:
                        v2.update(v10, 1)
        return v4
