class C1:

    def popcountDepth(self, a1, a2):
        if a2 == 0:
            return 1
        if a2 == 1:
            return a1.bit_length() - 1
        v1 = []
        v2 = a1
        while v2:
            v1.append(v2 % 2)
            v2 //= 2
        v1.reverse()
        v3 = len(v1)
        v4 = [0] * (v3 + 2)
        for v5 in range(2, v3 + 1):
            v6 = 0
            v7 = v5
            while v7 > 0:
                v6 += v7 & 1
                v7 >>= 1
            v4[v5] = 1 + v4[v6]
        v8 = [[[0 for v9 in range(2)] for v9 in range(v3 + 1)] for v9 in range(v3 + 1)]
        v8[0][0][1] = 1
        for v10 in range(v3):
            for v11 in range(v3 + 1):
                for v12 in range(2):
                    v13 = v8[v10][v11][v12]
                    if v13 == 0:
                        continue
                    v14 = v1[v10] if v12 == 1 else 1
                    for v15 in range(2):
                        if v15 > v14:
                            continue
                        v16 = 1 if v12 == 1 and v15 == v14 else 0
                        v17 = v11 + v15
                        if v17 > v3:
                            continue
                        v8[v10 + 1][v17][v16] += v13
        v18 = 0
        for v19 in range(2, v3 + 1):
            if v4[v19] == a2 - 1:
                v18 += v8[v3][v19][0] + v8[v3][v19][1]
        return v18
