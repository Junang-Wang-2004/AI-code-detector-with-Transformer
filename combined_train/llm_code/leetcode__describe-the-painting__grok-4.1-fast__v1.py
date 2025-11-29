class C1:

    def splitPainting(self, a1):
        v1 = []
        for v2, v3, v4 in a1:
            v1.append((v2, v4))
            v1.append((v3, -v4))
        v1.sort(key=lambda x: x[0])
        v5 = []
        v6 = 0
        v7 = None
        v8 = 0
        while v8 < len(v1):
            v9 = v1[v8][0]
            if v7 is not None and v6 > 0:
                v5.append([v7, v9, v6])
            while v8 < len(v1) and v1[v8][0] == v9:
                v6 += v1[v8][1]
                v8 += 1
            v7 = v9
        return v5
