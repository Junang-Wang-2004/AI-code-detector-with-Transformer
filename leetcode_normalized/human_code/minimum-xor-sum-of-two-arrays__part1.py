class C1(object):

    def minimumXORSum(self, a1, a2):

        def hungarian(a1):
            if not a1:
                return (0, [])
            v1, v2 = (len(a1) + 1, len(a1[0]) + 1)
            v3, v4, v5, v6 = ([0] * v1, [0] * v2, [0] * v2, [0] * (v1 - 1))
            for v7 in range(1, v1):
                v5[0] = v7
                v8 = 0
                v9, v10 = ([float('inf')] * v2, [-1] * v2)
                v11 = [False] * (v2 + 1)
                while True:
                    v11[v8] = True
                    v12, v13, v14 = (v5[v8], None, float('inf'))
                    for v15 in range(1, v2):
                        if v11[v15]:
                            continue
                        v16 = a1[v12 - 1][v15 - 1] - v3[v12] - v4[v15]
                        if v16 < v9[v15]:
                            v9[v15], v10[v15] = (v16, v8)
                        if v9[v15] < v14:
                            v14, v13 = (v9[v15], v15)
                    for v15 in range(v2):
                        if v11[v15]:
                            v3[v5[v15]] += v14
                            v4[v15] -= v14
                        else:
                            v9[v15] -= v14
                    v8 = v13
                    if not v5[v8]:
                        break
                while v8:
                    v13 = v10[v8]
                    v5[v8], v8 = (v5[v13], v13)
            for v15 in range(1, v2):
                if v5[v15]:
                    v6[v5[v15] - 1] = v15 - 1
            return (-v4[0], v6)
        v1 = [[0] * len(a2) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in range(len(a2)):
                v1[v3][v4] = a1[v3] ^ a2[v4]
        return hungarian(v1)[0]
