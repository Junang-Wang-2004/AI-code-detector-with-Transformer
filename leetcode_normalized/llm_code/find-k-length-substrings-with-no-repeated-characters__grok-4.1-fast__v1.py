class C1:

    def numKLenSubstrNoRepeats(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = {}
        for v4 in range(len(a1)):
            if a1[v4] in v3 and v3[a1[v4]] >= v2:
                v2 = v3[a1[v4]] + 1
            v3[a1[v4]] = v4
            if v4 - v2 + 1 >= a2:
                v1 += 1
        return v1
