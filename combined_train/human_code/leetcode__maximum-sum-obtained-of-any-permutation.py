import itertools

class C1(object):

    def maxSumRangeQuery(self, a1, a2):
        """
        """

        def addmod(a1, a2, a3):
            a1 %= a3
            a2 %= a3
            if a3 - a1 <= a2:
                a2 -= a3
            return a1 + a2

        def mulmod(a1, a2, a3):
            a1 %= a3
            a2 %= a3
            if a1 < a2:
                a1, a2 = (a2, a1)
            v3 = 0
            while a2 > 0:
                if a2 % 2 == 1:
                    v3 = addmod(v3, a1, a3)
                a1 = addmod(a1, a1, a3)
                a2 //= 2
            return v3
        v1 = 10 ** 9 + 7
        v2 = [0] * len(a1)
        for v3, v4 in a2:
            v2[v3] += 1
            if v4 + 1 < len(v2):
                v2[v4 + 1] -= 1
        for v5 in range(1, len(v2)):
            v2[v5] += v2[v5 - 1]
        a1.sort()
        v2.sort()
        v6 = 0
        for v5, (v7, v8) in enumerate(zip(a1, v2)):
            v6 = (v6 + v7 * v8) % v1
        return v6
