class C1:

    def maxProfit(self, a1, a2):
        v1 = len(a1)
        v2 = float('-inf')
        v3 = sorted(set(a1))
        v4 = len(v3)
        if v4 < 3:
            return -1
        v5 = {v3[i]: i + 1 for v6 in range(v4)}
        v7 = {v3[v6]: v4 - v6 for v6 in range(v4)}

        class MaxFenwick:

            def __init__(self, a1, a2):
                self.sz = a1
                self.default = a2
                self.t = [a2] * (a1 + 2)

            def upd(self, a1, a2):
                while a1 <= self.sz:
                    self.t[a1] = max(self.t[a1], a2)
                    a1 += a1 & -a1

            def q(self, a1):
                v1 = self.default
                while a1 > 0:
                    v1 = max(v1, self.t[a1])
                    a1 -= a1 & -a1
                return v1
        v8 = MaxFenwick(v4, v2)
        v9 = [v2] * v1
        for v6 in range(v1):
            v10 = v5[a1[v6]]
            v9[v6] = v8.q(v10 - 1) if v10 > 1 else v2
            v8.upd(v10, a2[v6])
        v11 = MaxFenwick(v4, v2)
        v12 = [v2] * v1
        for v6 in range(v1 - 1, -1, -1):
            v13 = v7[a1[v6]]
            v12[v6] = v11.q(v13 - 1) if v13 > 1 else v2
            v11.upd(v13, a2[v6])
        v14 = v2
        for v6 in range(v1):
            v14 = max(v14, v9[v6] + a2[v6] + v12[v6])
        return -1 if v14 == v2 else v14
