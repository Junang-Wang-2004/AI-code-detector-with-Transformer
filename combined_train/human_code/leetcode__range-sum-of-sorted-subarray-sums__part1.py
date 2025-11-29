class C1(object):

    def rangeSum(self, a1, a2, a3, a4):
        """
        """

        def countUntil(a1, a2):
            v1, v2, v3 = (0, 0, 0)
            for v4 in range(len(a1)):
                v2 += a1[v4]
                while v2 > a2:
                    v2 -= a1[v3]
                    v3 += 1
                v1 += v4 - v3 + 1
            return v1

        def sumUntil(a1, a2, a3):
            v1, v2, v3, v4 = (0, 0, 0, 0)
            for v5 in range(len(a1)):
                v2 += a1[v5]
                v3 += a1[v5] * (v5 - v4 + 1)
                while v2 > a3:
                    v2 -= a1[v4]
                    v3 -= a2[v5 + 1] - a2[v4 - 1 + 1]
                    v4 += 1
                v1 += v3
            return v1

        def sumLessOrEqualTo(a1, a2, a3, a4, a5):
            while a3 <= a4:
                v1 = a3 + (a4 - a3) // 2
                if countUntil(a2, v1) - a5 >= 0:
                    a4 = v1 - 1
                else:
                    a3 = v1 + 1
            return sumUntil(a2, a1, a3) - a3 * (countUntil(a2, a3) - a5)
        v1 = 10 ** 9 + 7
        v2 = [0] * (len(a1) + 1)
        for v3 in range(len(a1)):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4, v5 = (min(a1), sum(a1))
        return (sumLessOrEqualTo(v2, a1, v4, v5, a4) - sumLessOrEqualTo(v2, a1, v4, v5, a3 - 1)) % v1
