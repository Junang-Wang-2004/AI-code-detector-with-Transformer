import math

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 1e-15

        def count(a1, a2):
            return int(a2 - a1 + v2)
        if a3 == 1:
            return a1
        v3 = sorted(((log(x) / log(a3), i) for v4, v5 in enumerate(a1)))
        v6 = 0
        for v7 in range(1, int(v3[-1][0]) + 1 + 1):
            while v6 < len(v3) and count(v3[v6][0], v7) >= 1:
                v6 += 1
            if a2 - v6 < 0:
                v7 -= 1
                break
            a2 -= v6
        for v9, (v5, v4) in enumerate(v3):
            v10 = count(v5, v7)
            if v10 <= 0:
                break
            a1[v4] *= pow(a3, v10)
        v11, v12 = divmod(a2, len(a1))
        v13 = pow(a3, v11, v1)
        v14 = [0] * len(a1)
        for v9, (v5, v4) in enumerate(sorted(((v5, v4) for v4, v5 in enumerate(a1)))):
            v14[v4] = v5 * v13 * (a3 if v9 < v12 else 1) % v1
        return v14
