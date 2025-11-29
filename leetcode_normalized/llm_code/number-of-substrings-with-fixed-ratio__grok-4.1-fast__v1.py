class C1:

    def fixedRatio(self, a1, a2, a3):
        v1 = {0: 1}
        v2 = 0
        v3 = 0
        for v4 in a1:
            if v4 == '1':
                v3 += a2
            else:
                v3 -= a3
            v2 += v1.get(v3, 0)
            if v3 in v1:
                v1[v3] += 1
            else:
                v1[v3] = 1
        return v2
