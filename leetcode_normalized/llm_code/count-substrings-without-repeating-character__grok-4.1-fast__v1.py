class C1:

    def numberOfSpecialSubstrings(self, a1):
        v1 = 0
        v2 = 0
        v3 = {}
        for v4 in range(len(a1)):
            v5 = a1[v4]
            if v5 in v3 and v3[v5] >= v2:
                v2 = v3[v5] + 1
            v3[v5] = v4
            v1 += v4 - v2 + 1
        return v1
