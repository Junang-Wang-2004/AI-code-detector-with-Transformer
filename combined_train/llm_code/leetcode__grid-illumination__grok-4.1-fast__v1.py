import collections

class C1(object):

    def gridIllumination(self, a1, a2, a3):
        v1 = set()
        v2 = collections.defaultdict(int)
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)
        v5 = collections.defaultdict(int)
        for v6 in a2:
            v7, v8 = v6
            v9 = (v7, v8)
            if v9 in v1:
                continue
            v1.add(v9)
            v2[v7] += 1
            v3[v8] += 1
            v4[v7 - v8] += 1
            v5[v7 + v8] += 1
        v10 = []
        for v11 in a3:
            v12, v13 = v11
            v14 = v12 - v13
            v15 = v12 + v13
            v16 = v2[v12] or v3[v13] or v4[v14] or v5[v15]
            if not v16:
                v10.append(0)
                continue
            v10.append(1)
            for v17 in (-1, 0, 1):
                for v18 in (-1, 0, 1):
                    v19 = v12 + v17
                    v20 = v13 + v18
                    if 0 <= v19 < a1 and 0 <= v20 < a1:
                        v21 = (v19, v20)
                        if v21 in v1:
                            v1.discard(v21)
                            v2[v19] -= 1
                            v3[v20] -= 1
                            v4[v19 - v20] -= 1
                            v5[v19 + v20] -= 1
        return v10
