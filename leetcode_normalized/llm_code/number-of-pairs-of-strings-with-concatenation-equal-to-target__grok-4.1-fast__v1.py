class C1:

    def numOfPairs(self, a1, a2):
        v1 = {}
        v2 = {}
        v3 = 0
        v4 = len(a2)
        for v5 in a1:
            v6 = len(v5)
            v7 = v4 - v6
            v8 = v5 == a2[:v6]
            v9 = v5 == a2[-v6:]
            if v8:
                v3 += v2.get(v7, 0)
            if v9:
                v3 += v1.get(v7, 0)
            if v8:
                v1[v6] = v1.get(v6, 0) + 1
            if v9:
                v2[v6] = v2.get(v6, 0) + 1
        return v3
