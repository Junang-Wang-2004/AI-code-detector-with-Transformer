import collections

class C1(object):

    def squareFreeSubsets(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = max(a1)
        v3 = list(range(v2 + 1))
        for v4 in range(2, int(v2 ** 0.5) + 1):
            if v3[v4] == v4:
                for v5 in range(v4 * v4, v2 + 1, v4):
                    if v3[v5] == v5:
                        v3[v5] = v4
        v6 = [v4 for v4 in range(2, v2 + 1) if v3[v4] == v4]
        v7 = {p: v4 for v4, v8 in enumerate(v6)}
        v9 = collections.Counter(a1)
        v10 = v9[1]
        v11 = []
        for v12, v13 in v9.items():
            if v12 == 1:
                continue
            v14 = v12
            v15 = 0
            v16 = True
            while v14 > 1:
                v8 = v3[v14]
                v17 = 1 << v7[v8]
                v15 |= v17
                v14 //= v8
                if v14 % v8 == 0:
                    v16 = False
                    break
            if v16:
                v11.append((v15, v13))
        v18 = len(v6)
        v19 = (1 << v18) - 1
        v20 = [1] * (1 << v18)
        for v21, v13 in v11:
            v22 = [0] * (1 << v18)
            for v23 in range(1 << v18):
                if v20[v23] == 0:
                    continue
                v22[v23] = (v22[v23] + v20[v23]) % v1
                if v23 & v21 == 0:
                    v24 = v23 | v21
                    v22[v24] = (v22[v24] + v13 * v20[v23]) % v1
            v20 = v22
        v25 = (v20[v19] * pow(2, v10, v1) - 1) % v1
        return v25
