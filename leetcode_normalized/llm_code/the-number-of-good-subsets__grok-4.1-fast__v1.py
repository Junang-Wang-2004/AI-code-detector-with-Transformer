import collections

class C1:

    def numberOfGoodSubsets(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = max(a1)
        v3 = [True] * (v2 + 1)
        v3[0] = v3[1] = False
        for v4 in range(2, int(v2 ** 0.5) + 1):
            if v3[v4]:
                for v5 in range(v4 * v4, v2 + 1, v4):
                    v3[v5] = False
        v6 = [v4 for v4 in range(2, v2 + 1) if v3[v4]]
        v7 = 1 << len(v6)
        v8 = collections.Counter(a1)
        v9 = v8.pop(1, 0)
        v10 = [0] * v7
        v10[0] = 1
        for v11, v12 in list(v8.items()):
            v13 = 0
            v14 = True
            for v15, v16 in enumerate(v6):
                if v11 % (v16 * v16) == 0:
                    v14 = False
                    break
                if v11 % v16 == 0:
                    v13 |= 1 << v15
            if not v14:
                continue
            for v17 in range(v7):
                if v17 & v13 == 0:
                    v18 = v17 | v13
                    v10[v18] = (v10[v18] + v10[v17] * v12) % v1
        v19 = sum(v10) % v1
        v20 = (pow(2, v9, v1) * v19 - 1) % v1
        return v20
