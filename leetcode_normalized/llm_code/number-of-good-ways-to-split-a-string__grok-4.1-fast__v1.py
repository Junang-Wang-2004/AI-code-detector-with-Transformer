class C1:

    def numSplits(self, a1):
        v1 = ord('a')
        v2 = [0] * 26
        v3 = [0] * 26
        for v4 in a1:
            v3[ord(v4) - v1] += 1
        v5 = sum((1 for v6 in v3 if v6 > 0))
        v7 = 0
        v8 = 0
        for v4 in a1:
            v9 = ord(v4) - v1
            v2[v9] += 1
            if v2[v9] == 1:
                v7 += 1
            v3[v9] -= 1
            if v3[v9] == 0:
                v5 -= 1
            if v7 == v5:
                v8 += 1
        return v8
