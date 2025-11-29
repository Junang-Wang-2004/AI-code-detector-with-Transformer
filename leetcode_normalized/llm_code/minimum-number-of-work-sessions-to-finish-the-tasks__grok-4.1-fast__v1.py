class C1:

    def minSessions(self, a1, a2):
        v1 = len(a1)
        v2 = 1 << v1
        v3 = float('inf')
        v4 = [v3] * v2
        v5 = [v3] * v2
        v4[0] = 0
        v5[0] = a2 + 1
        for v6 in range(v2):
            if v4[v6] == v3:
                continue
            v7 = 1
            for v8 in a1:
                if v6 & v7:
                    v7 <<= 1
                    continue
                v9 = v6 | v7
                v10 = v5[v6]
                if v10 + v8 <= a2:
                    v11 = v4[v6]
                    v12 = v10 + v8
                else:
                    v11 = v4[v6] + 1
                    v12 = v8
                if v11 < v4[v9] or (v11 == v4[v9] and v12 < v5[v9]):
                    v4[v9] = v11
                    v5[v9] = v12
                v7 <<= 1
        return v4[v2 - 1]
