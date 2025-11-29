class C1(object):

    def findRLEArray(self, a1, a2):
        v1 = iter(a1)
        v2 = iter(a2)
        v3 = []
        v4 = next(v1, None)
        v5 = next(v2, None)
        while v4 is not None and v5 is not None:
            v6, v7 = v4
            v8, v9 = v5
            v10 = min(v7, v9)
            v11 = v6 * v8
            if v3 and v3[-1][0] == v11:
                v3[-1][1] += v10
            else:
                v3.append([v11, v10])
            v7 -= v10
            v9 -= v10
            if v7 == 0:
                v4 = next(v1, None)
            if v9 == 0:
                v5 = next(v2, None)
        return v3
