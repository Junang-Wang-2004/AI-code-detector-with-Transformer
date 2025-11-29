class C1(object):

    def kthSmallest(self, a1, a2):
        """
        """

        def countArraysHaveSumLessOrEqual(a1, a2, a3, a4):
            if a4 < 0:
                return 0
            if a3 == len(a1):
                return 1
            v1 = 0
            for v2 in range(len(a1[0])):
                v3 = countArraysHaveSumLessOrEqual(a1, a2 - v1, a3 + 1, a4 - a1[a3][v2])
                if not v3:
                    break
                v1 += v3
                if v1 > a2:
                    break
            return v1
        v1 = max((x for v2 in a1 for v3 in v2))
        v4, v5 = (len(a1), len(a1) * v1)
        while v4 <= v5:
            v6 = v4 + (v5 - v4) // 2
            v7 = countArraysHaveSumLessOrEqual(a1, a2, 0, v6)
            if v7 >= a2:
                v5 = v6 - 1
            else:
                v4 = v6 + 1
        return v4
