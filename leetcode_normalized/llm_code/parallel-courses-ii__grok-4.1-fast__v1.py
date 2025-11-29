class C1:

    def minNumberOfSemesters(self, a1, a2, a3):
        v1 = [0] * a1
        for v2, v3 in a2:
            v1[v3 - 1] |= 1 << v2 - 1
        v4 = a1 + 1
        v5 = [v4] * (1 << a1)
        v5[0] = 0
        v6 = [0] * (1 << a1)
        for v7 in range(1 << a1):
            v6[v7] = v6[v7 // 2] + (v7 & 1)
        for v8 in range(1 << a1):
            if v5[v8] == v4:
                continue
            v9 = 0
            for v7 in range(a1):
                if v8 & 1 << v7 == 0 and v8 & v1[v7] == v1[v7]:
                    v9 |= 1 << v7
            v10 = v6[v9]
            v11 = min(v10, a3)
            v12 = v9
            while v12:
                if v6[v12] == v11:
                    v13 = v8 | v12
                    v5[v13] = min(v5[v13], v5[v8] + 1)
                v12 = v12 - 1 & v9
        return v5[(1 << a1) - 1]
