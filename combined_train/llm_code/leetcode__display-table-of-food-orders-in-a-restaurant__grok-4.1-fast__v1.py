class C1:

    def displayTable(self, a1):
        v1 = set()
        v2 = set()
        for v3, v4, v5 in a1:
            v1.add(int(v4))
            v2.add(v5)
        v6 = sorted(v1)
        v7 = sorted(v2)
        v8 = {t: {d: 0 for v9 in v7} for v10 in v6}
        for v3, v4, v5 in a1:
            v10 = int(v4)
            v8[v10][v5] += 1
        v11 = [['Table'] + v7]
        for v10 in v6:
            v12 = [str(v10)]
            for v9 in v7:
                v12.append(str(v8[v10][v9]))
            v11.append(v12)
        return v11
