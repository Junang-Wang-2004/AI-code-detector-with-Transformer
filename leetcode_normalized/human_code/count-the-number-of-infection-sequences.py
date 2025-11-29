v1, v2, v3 = [[1] * 2 for v4 in range(3)]

class C1(object):

    def numberOfSequence(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def nCr(a1, a2):
            while len(v2) <= a1:
                v1.append(v1[-1] * len(v2) % v1)
                v2.append(v2[v1 % len(v2)] * (v1 - v1 // len(v2)) % v1)
                v3.append(v3[-1] * v2[-1] % v1)
            return v1[a1] * v3[a1 - a2] % v1 * v3[a2] % v1
        v2 = 1
        v3 = v4 = 0
        for v5 in range(len(a2) + 1):
            v6 = (a2[v5] if v5 < len(a2) else a1) - (a2[v5 - 1] if v5 - 1 >= 0 else -1) - 1
            if v5 not in (0, len(a2)):
                v4 += max(v6 - 1, 0)
            v3 += v6
            v2 = v2 * nCr(v3, v6) % v1
        v2 = v2 * pow(2, v4, v1) % v1
        return v2
