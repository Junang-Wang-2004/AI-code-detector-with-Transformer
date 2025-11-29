class C1:

    def maximumTripletValue(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v2[v1 - 1] = a1[v1 - 1]
        for v3 in range(v1 - 2, -1, -1):
            v2[v3] = max(v2[v3 + 1], a1[v3])
        v4 = sorted(set(a1))
        v5 = {v4[v3]: v3 + 1 for v3 in range(len(v4))}
        v6 = len(v4)
        v7 = [-1] * (v6 + 2)

        def upd(a1, a2):
            while a1 <= v6:
                v7[a1] = max(v7[a1], a2)
                a1 += a1 & -a1

        def qmax(a1):
            v1 = -1
            while a1 > 0:
                v1 = max(v1, v7[a1])
                a1 -= a1 & -a1
            return v1
        v8 = 0
        for v9 in range(v1):
            if 1 <= v9 < v1 - 1:
                v10 = v5[a1[v9]]
                v11 = qmax(v10 - 1)
                v12 = v2[v9 + 1]
                if v11 != -1 and v12 > a1[v9]:
                    v8 = max(v8, v11 - a1[v9] + v12)
            upd(v5[a1[v9]], a1[v9])
        return v8
