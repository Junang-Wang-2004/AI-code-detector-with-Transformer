class C1:

    def getRow(self, a1):
        v1 = [1] * (a1 + 1)
        for v2 in range(2, a1 + 1):
            for v3 in range(v2 - 1, 0, -1):
                v1[v3] += v1[v3 - 1]
        return v1
