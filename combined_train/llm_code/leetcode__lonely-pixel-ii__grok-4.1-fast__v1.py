class C1(object):

    def findBlackPixel(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]) if a1 else 0)
        if v1 == 0 or v2 == 0:
            return 0
        v3 = [0] * v2
        for v4 in a1:
            for v5, v6 in enumerate(v4):
                if v6 == 'B':
                    v3[v5] += 1
        v7 = {}
        for v8 in a1:
            if v8 not in v7:
                v7[v8] = [0, v8.count('B')]
            v7[v8][0] += 1
        v9 = 0
        for v8, (v10, v11) in v7.items():
            if v10 == a2 and v11 == a2:
                v12 = 0
                for v5 in range(v2):
                    if v8[v5] == 'B' and v3[v5] == a2:
                        v12 += 1
                v9 += v12 * a2
        return v9
