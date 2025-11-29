from functools import reduce

class C1(object):

    def kInversePairs(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * (a2 + 1)
        v2[0] = 1
        for v3 in range(a1):
            v4 = [0] * len(v2)
            v5 = 0
            for v6 in range(len(v2)):
                v5 = (v5 + v2[v6]) % v1
                if v6 - (v3 + 1) >= 0:
                    v5 = (v5 - v2[v6 - (v3 + 1)]) % v1
                v4[v6] = v5
            v2 = v4
        return v2[-1]
