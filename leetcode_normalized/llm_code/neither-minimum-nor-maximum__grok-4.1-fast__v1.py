class C1:

    def findNonMinOrMax(self, a1):
        if len(a1) < 3:
            return -1
        v1 = v2 = a1[0]
        for v3 in a1:
            if v3 < v1:
                v1 = v3
            elif v3 > v2:
                v2 = v3
        for v3 in a1:
            if v1 < v3 < v2:
                return v3
        return -1
