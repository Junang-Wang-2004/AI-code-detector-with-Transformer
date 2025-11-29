class C1:

    def findPattern(self, a1, a2):
        v1 = len(a2)
        if v1 == 0:
            return 0
        v2 = [0] * v1
        v3 = 0
        v4 = 1
        while v4 < v1:
            if a2[v4] == a2[v3]:
                v3 += 1
                v2[v4] = v3
                v4 += 1
            elif v3 != 0:
                v3 = v2[v3 - 1]
            else:
                v2[v4] = 0
                v4 += 1
        v5 = 0
        v6 = 0
        while True:
            v7 = next(a1)
            while v6 > 0 and a2[v6] != v7:
                v6 = v2[v6 - 1]
            if a2[v6] == v7:
                v6 += 1
            if v6 == v1:
                return v5 - v1 + 1
            v5 += 1
