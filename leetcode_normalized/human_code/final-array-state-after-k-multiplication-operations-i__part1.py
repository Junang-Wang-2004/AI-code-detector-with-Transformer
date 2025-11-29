import math

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        v1 = 1e-15

        def count(a1, a2):
            return int(a2 - a1 + v1)
        if a3 == 1:
            return a1
        v2 = sorted(((log(x) / log(a3), i) for v3, v4 in enumerate(a1)))
        v5 = 0
        for v6 in range(1, int(v2[-1][0]) + 1 + 1):
            while v5 < len(v2) and count(v2[v5][0], v6) >= 1:
                v5 += 1
            if a2 - v5 < 0:
                v6 -= 1
                break
            a2 -= v5
        for v8, (v4, v3) in enumerate(v2):
            v9 = count(v4, v6)
            if v9 <= 0:
                break
            a1[v3] *= pow(a3, v9)
        v10, v11 = divmod(a2, len(a1))
        v12 = pow(a3, v10)
        v13 = [0] * len(a1)
        for v8, (v4, v3) in enumerate(sorted(((v4, v3) for v3, v4 in enumerate(a1)))):
            v13[v3] = v4 * v12 * (a3 if v8 < v11 else 1)
        return v13
