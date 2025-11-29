class C1(object):

    def arithmeticTriplets(self, a1, a2):
        v1 = {}
        for v2, v3 in enumerate(a1):
            v1.setdefault(v3, []).append(v2)
        v4 = 0
        for v5 in v1:
            v6 = v5 + a2
            v7 = v6 + a2
            if v6 in v1 and v7 in v1:
                v4 += len(v1[v5]) * len(v1[v6]) * len(v1[v7])
        return v4
