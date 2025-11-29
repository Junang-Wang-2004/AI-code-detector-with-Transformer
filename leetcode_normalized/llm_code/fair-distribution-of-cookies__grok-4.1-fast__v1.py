class C1(object):

    def distributeCookies(self, a1, a2):
        v1 = len(a1)
        v2 = (1 << v1) - 1
        v3 = [0] * (1 << v1)
        for v4 in range(v1):
            v5 = 1 << v4
            for v6 in range(1 << v1):
                if v6 & v5:
                    v3[v6] += a1[v4]
        v7 = float('inf')
        v8 = [[v7] * (1 << v1) for v9 in range(a2 + 1)]
        v8[0][0] = 0
        for v10 in range(1, a2 + 1):
            for v6 in range(1 << v1):
                v11 = v6
                while v11:
                    v12 = v3[v11]
                    v13 = v6 ^ v11
                    v14 = v8[v10 - 1][v13]
                    v8[v10][v6] = min(v8[v10][v6], max(v12, v14))
                    v11 = v11 - 1 & v6
        return v8[a2][v2]
