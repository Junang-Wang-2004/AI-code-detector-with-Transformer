class C1:

    def bestTeamScore(self, a1, a2):
        v1 = len(a1)
        v2 = sorted(zip(a2, a1))
        v3 = sorted(set(a1))
        v4 = len(v3)
        v5 = {v3[j]: j + 1 for v6 in range(v4)}
        v7 = [0] * (v4 + 2)

        def up(a1, a2):
            while a1 <= v4:
                v7[a1] = max(v7[a1], a2)
                a1 += a1 & -a1

        def q(a1):
            v1 = 0
            while a1 > 0:
                v1 = max(v1, v7[a1])
                a1 -= a1 & -a1
            return v1
        v8 = 0
        while v8 < v1:
            v9 = v2[v8][0]
            v10 = []
            while v8 < v1 and v2[v8][0] == v9:
                v10.append(v2[v8][1])
                v8 += 1
            v11 = []
            for v12 in v10:
                v13 = v5[v12]
                v14 = q(v13)
                v11.append((v13, v14 + v12))
            for v13, v15 in v11:
                up(v13, v15)
        return q(v4)
