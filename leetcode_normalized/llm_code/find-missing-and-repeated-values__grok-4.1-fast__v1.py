class C1(object):

    def findMissingAndRepeatedValues(self, a1):
        v1 = len(a1)
        v2 = v1 * v1
        v3 = v2 * (v2 + 1) // 2
        v4 = v2 * (v2 + 1) * (2 * v2 + 1) // 6
        v5 = 0
        v6 = 0
        for v7 in a1:
            for v8 in v7:
                v5 += v8
                v6 += v8 * v8
        v9 = v5 - v3
        v10 = v6 - v4
        v11 = v10 // v9
        v12 = (v11 + v9) // 2
        v13 = (v11 - v9) // 2
        return [v12, v13]
