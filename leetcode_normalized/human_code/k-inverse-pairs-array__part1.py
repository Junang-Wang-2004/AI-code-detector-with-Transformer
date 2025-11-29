from functools import reduce

class C1(object):

    def kInversePairs(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [1]
        for v3 in range(a1):
            v4 = [0] * min(len(v2) + (v3 + 1 - 1), a2 + 1)
            for v5 in range(len(v4)):
                v4[v5] = v2[v5] if v5 < len(v2) else 0
                if v5 - 1 >= 0:
                    v4[v5] = (v4[v5] + v4[v5 - 1]) % v1
                if v5 - (v3 + 1) >= 0:
                    v4[v5] = (v4[v5] - v2[v5 - (v3 + 1)]) % v1
            v2 = v4
        return v2[a2] if a2 < len(v2) else 0
