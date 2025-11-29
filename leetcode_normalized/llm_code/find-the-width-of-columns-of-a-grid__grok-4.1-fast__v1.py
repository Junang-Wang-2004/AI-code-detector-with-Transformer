class C1:

    def findColumnWidth(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return []
        v2 = len(a1[0])
        v3 = [0] * v2
        for v4 in range(v2):
            v5 = 0
            for v6 in range(v1):
                v7 = str(a1[v6][v4])
                v5 = max(v5, len(v7))
            v3[v4] = v5
        return v3
