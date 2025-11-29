import math

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        v1 = 1e-15

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def count(a1, a2):
            return int(a2 - a1 + v1)

        def check(a1):
            v1 = 0
            for v2, v3 in vals:
                v4 = count(v2, a1)
                if v4 <= 0:
                    break
                v1 += v4
            return v1 <= a2
        if a3 == 1:
            return a1
        v2 = sorted(((log(x) / log(a3), i) for v3, v4 in enumerate(a1)))
        v5 = binary_search_right(1, int(v2[-1][0]) + 1, check)
        for v6, (v4, v3) in enumerate(v2):
            v7 = count(v4, v5)
            if v7 <= 0:
                break
            a2 -= v7
            a1[v3] *= pow(a3, v7)
        v9, v10 = divmod(a2, len(a1))
        v11 = pow(a3, v9)
        v12 = [0] * len(a1)
        for v6, (v4, v3) in enumerate(sorted(((v4, v3) for v3, v4 in enumerate(a1)))):
            v12[v3] = v4 * v11 * (a3 if v6 < v10 else 1)
        return v12
