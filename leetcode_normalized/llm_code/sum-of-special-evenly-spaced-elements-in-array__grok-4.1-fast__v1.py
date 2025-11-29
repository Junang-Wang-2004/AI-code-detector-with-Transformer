class C1(object):

    def solve(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = []
        v4 = int(v2 ** 0.5) + 1
        v5 = {}
        for v6 in range(1, v4 + 1):
            v5[v6] = [[] for v7 in range(v6)]
            for v8 in range(v6):
                v9 = [0]
                v10 = v8
                while v10 < v2:
                    v9.append((v9[-1] + a1[v10]) % v1)
                    v10 += v6
                v5[v6][v8] = v9
        for v11, v12 in a2:
            if v12 * v12 > v2:
                v13 = 0
                v14 = v11
                while v14 < v2:
                    v13 = (v13 + a1[v14]) % v1
                    v14 += v12
                v3.append(v13)
            else:
                v8 = v11 % v12
                v9 = v5[v12][v8]
                v15 = len(v9) - 1
                v16 = min(v11 // v12, v15)
                v13 = (v9[-1] - v9[v16] + v1) % v1
                v3.append(v13)
        return v3
