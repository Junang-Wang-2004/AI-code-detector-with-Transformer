import math

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 1e-15

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def count(a1, a2):
            return int(a2 - a1 + v2)

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
        v3 = sorted(((log(x) / log(a3), i) for v4, v5 in enumerate(a1)))
        v6 = binary_search_right(1, int(v3[-1][0]) + 1, check)
        for v7, (v5, v4) in enumerate(v3):
            v8 = count(v5, v6)
            if v8 <= 0:
                break
            a2 -= v8
            a1[v4] *= pow(a3, v8)
        v10, v11 = divmod(a2, len(a1))
        v12 = pow(a3, v10, v1)
        v13 = [0] * len(a1)
        for v7, (v5, v4) in enumerate(sorted(((v5, v4) for v4, v5 in enumerate(a1)))):
            v13[v4] = v5 * v12 * (a3 if v7 < v11 else 1) % v1
        return v13
