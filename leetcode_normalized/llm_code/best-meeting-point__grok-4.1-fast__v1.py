class C1:

    def minTotalDistance(self, a1):
        v1 = []
        v2 = []
        v3 = len(a1)
        v4 = len(a1[0]) if a1 else 0
        for v5 in range(v3):
            for v6 in range(v4):
                if a1[v5][v6] == 1:
                    v1.append(v5)
                    v2.append(v6)
        v1.sort()
        v2.sort()
        v7 = len(v1)
        if v7 == 0:
            return 0
        v8 = v1[v7 // 2]
        v9 = v2[v7 // 2]
        v10 = 0
        for v11 in v1:
            v10 += abs(v11 - v8)
        for v12 in v2:
            v10 += abs(v12 - v9)
        return v10
