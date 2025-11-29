import collections

class C1:

    def countTrapezoids(self, a1):

        def reduce_frac(a1, a2):
            v1 = 0
            v2, v3 = (abs(a1), abs(a2))
            while v3:
                v2, v3 = (v3, v2 % v3)
            v1 = v2
            if v1 == 0:
                return (0, 0)
            v4 = a1 // v1
            v5 = a2 // v1
            if v4 < 0 or (v4 == 0 and v5 < 0):
                v4, v5 = (-v4, -v5)
            return (v4, v5)
        v1 = collections.defaultdict(int)
        v2 = collections.defaultdict(int)
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)
        v5 = 0
        v6 = 0
        v7 = len(a1)
        for v8 in range(v7):
            v9, v10 = a1[v8]
            for v11 in range(v8):
                v12, v13 = a1[v11]
                v14 = v12 - v9
                v15 = v13 - v10
                v16, v17 = reduce_frac(v14, v15)
                if v16 == 0 and v17 == 0:
                    continue
                v18 = v17 * v9 - v16 * v10
                v19 = (v16, v17, v18)
                v20 = v14 * v14 + v15 * v15
                v21 = (v16, v17, v20)
                v22 = (v16, v17, v18, v20)
                v5 += v1[v16, v17] - v2[v19]
                v6 += v3[v21] - v4[v22]
                v1[v16, v17] += 1
                v2[v19] += 1
                v3[v21] += 1
                v4[v22] += 1
        return v5 - v6 // 2
