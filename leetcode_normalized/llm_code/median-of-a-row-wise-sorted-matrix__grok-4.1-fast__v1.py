class C1(object):

    def matrixMedian(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = v1 * v2

        def count_less_equal(a1, a2):
            v1, v2 = (0, v2)
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if a1[v3] <= a2:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1

        def exceeds_half(a1):
            v1 = 0
            for v2 in a1:
                v1 += count_less_equal(v2, a1)
            return v1 > v3 // 2
        v4 = min((row[0] for v5 in a1))
        v6 = max((v5[-1] for v5 in a1))
        v7, v8 = (v4, v6)
        while v7 <= v8:
            v9 = v7 + (v8 - v7) // 2
            if exceeds_half(v9):
                v8 = v9 - 1
            else:
                v7 = v9 + 1
        return v7
