class C1(object):

    def minNumberOfHours(self, a1, a2, a3, a4):
        v1 = 0
        v2 = a1
        v3 = a2
        v4 = len(a3)
        for v5 in range(v4):
            v6 = a3[v5]
            v7 = a4[v5]
            if v2 <= v6:
                v8 = v6 + 1 - v2
                v1 += v8
                v2 += v8
            v2 -= v6
            if v3 <= v7:
                v8 = v7 + 1 - v3
                v1 += v8
                v3 += v8
            v3 += v7
        return v1
