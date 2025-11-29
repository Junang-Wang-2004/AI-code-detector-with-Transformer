class C1:

    def getMaximumGenerated(self, a1):
        v1 = {}
        v2 = 0
        for v3 in range(a1 + 1):
            if v3 == 0:
                v4 = 0
            elif v3 == 1:
                v4 = 1
            else:
                v5 = v3 // 2
                v4 = v1[v5] if v3 % 2 == 0 else v1[v5] + v1[v5 + 1]
            v1[v3] = v4
            if v4 > v2:
                v2 = v4
        return v2
