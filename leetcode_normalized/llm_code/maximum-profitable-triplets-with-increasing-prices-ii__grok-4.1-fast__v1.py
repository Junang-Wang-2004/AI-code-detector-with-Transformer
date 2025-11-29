class C1:

    def maxProfit(self, a1, a2):
        v1 = float('-inf')
        if len(a1) < 3:
            return -1
        v2 = sorted(set(a1))
        v3 = {val: i for v4, v5 in enumerate(v2)}
        v6 = len(v2)

        class MaxFenwick:

            def __init__(self, a1):
                self.n = a1
                self.data = [v1] * (a1 + 2)

            def modify(self, a1, a2):
                a1 += 1
                while a1 <= self.n:
                    self.data[a1] = max(self.data[a1], a2)
                    a1 += a1 & -a1

            def prefix_max(self, a1):
                if a1 < 0:
                    return v1
                a1 += 1
                v2 = v1
                while a1 > 0:
                    v2 = max(v2, self.data[a1])
                    a1 -= a1 & -a1
                return v2
        v7 = MaxFenwick(v6)
        v8 = MaxFenwick(v6)
        v9 = v1
        for v4 in range(len(a1)):
            v10 = a1[v4]
            v11 = a2[v4]
            v12 = v3[v10]
            v13 = v8.prefix_max(v12 - 1)
            v9 = max(v9, v13 + v11)
            v14 = v7.prefix_max(v12 - 1)
            v7.modify(v12, v11)
            v8.modify(v12, v14 + v11)
        return v9 if v9 != v1 else -1
