class C1:

    def buildWall(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = [set() for v3 in range(a2 + 1)]
        v2[0].add(0)
        for v4 in range(a2):
            for v5 in v2[v4]:
                for v6 in a3:
                    v7 = v4 + v6
                    if v7 > a2:
                        continue
                    v8 = v5 | 1 << v7
                    v2[v7].add(v8)
        v9 = [m ^ 1 << a2 for v10 in v2[a2]]
        v11 = len(v9)
        v12 = [[k for v13 in range(v11) if v9[v13] & v9[j] == 0] for v14 in range(v11)]
        v15 = [1] * v11
        for v3 in range(a1 - 1):
            v16 = [0] * v11
            for v14 in range(v11):
                v17 = 0
                for v13 in v12[v14]:
                    v17 = (v17 + v15[v13]) % v1
                v16[v14] = v17
            v15 = v16
        return sum(v15) % v1
