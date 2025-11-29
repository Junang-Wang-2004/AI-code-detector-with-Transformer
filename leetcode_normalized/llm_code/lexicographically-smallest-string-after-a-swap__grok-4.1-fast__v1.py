class C1:

    def getSmallestString(self, a1):
        v1 = len(a1)
        for v2 in range(v1 - 1):
            v3 = int(a1[v2])
            v4 = int(a1[v2 + 1])
            if v3 % 2 == v4 % 2 and v3 > v4:
                return a1[:v2] + str(v4) + str(v3) + a1[v2 + 2:]
        return a1
