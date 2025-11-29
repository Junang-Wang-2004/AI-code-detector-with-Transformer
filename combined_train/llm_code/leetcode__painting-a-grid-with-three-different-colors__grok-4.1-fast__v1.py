import collections

class C1(object):

    def colorTheGrid(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2, v3 = (min(a1, a2), max(a1, a2))
        if v2 == 0:
            return 1

        def get_valid_masks(a1):
            v1 = [0]
            v2 = 1
            for v3 in range(a1):
                v4 = []
                for v5 in v1:
                    v6 = v5 // (v2 // 3) % 3 if v2 > 1 else -1
                    for v7 in range(3):
                        if v7 == v6:
                            continue
                        v4.append(v5 + v7 * v2)
                v1 = v4
                v2 *= 3
            return v1

        def get_compat_curr(a1, a2):
            v1 = [0]
            v2 = 1
            for v3 in range(a1):
                v4 = []
                for v5 in v1:
                    v6 = v5 // (v2 // 3) % 3 if v2 > 1 else -1
                    v7 = a2 // v2 % 3
                    for v8 in range(3):
                        if v8 == v6 or v8 == v7:
                            continue
                        v4.append(v5 + v8 * v2)
                v1 = v4
                v2 *= 3
            return v1

        def get_canon(a1, a2):
            v1 = {}
            v2 = 0
            v3 = 0
            v4 = 1
            for v5 in range(a1):
                v6 = a2 // v4 % 3
                if v6 not in v1:
                    v1[v6] = v2
                    v2 += 1
                v3 += v1[v6] * v4
                v4 *= 3
            return v3
        v4 = get_valid_masks(v2)
        v5 = collections.Counter((get_canon(v2, rm) for v6 in v4))
        if v3 == 1:
            return sum(v5.values()) % v1
        v7 = sorted(v5)
        v8 = len(v7)
        v9 = {v7[i]: i for v10 in range(v8)}
        v11 = [[0] * v8 for v12 in range(v8)]
        for v10 in range(v8):
            v13 = v7[v10]
            v14 = get_compat_curr(v2, v13)
            v15 = collections.Counter((get_canon(v2, nr) for v16 in v14))
            for v17, v18 in v15.items():
                v19 = v9[v17]
                v11[v10][v19] = v18 % v1

        def matrix_multiply(a1, a2, a3):
            v1, v2 = (len(a1), len(a1[0]))
            v3 = len(a2[0])
            v4 = [[0] * v3 for v12 in range(v1)]
            for v5 in range(v1):
                for v6 in range(v2):
                    if a1[v5][v6] == 0:
                        continue
                    v7 = a1[v5][v6]
                    for v8 in range(v3):
                        v4[v5][v8] = (v4[v5][v8] + v7 * a2[v6][v8]) % a3
            return v4

        def matrix_power(a1, a2, a3):
            v1 = len(a1)
            v2 = [[1 if ii == jj else 0 for v3 in range(v1)] for v4 in range(v1)]
            while a2 > 0:
                if a2 & 1:
                    v2 = matrix_multiply(v2, a1, a3)
                a1 = matrix_multiply(a1, a1, a3)
                a2 >>= 1
            return v2
        v20 = [[v5[v7[v10]] for v10 in range(v8)]]
        v21 = matrix_power(v11, v3 - 1, v1)
        v22 = matrix_multiply(v20, v21, v1)
        return sum(v22[0]) % v1
