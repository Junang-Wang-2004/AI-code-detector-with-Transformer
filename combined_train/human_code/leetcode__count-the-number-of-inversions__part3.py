from functools import reduce

class C1(object):

    def numberOfPermutations(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [-1] * a1
        for v3, v4 in a2:
            v2[v3] = v4
        v5 = [0] * (v2[-1] + 1)
        v5[0] = 1
        for v3 in range(a1):
            v6 = [0] * len(v5)
            v7 = 0
            for v8 in range(len(v5)):
                v7 = (v7 + v5[v8]) % v1
                if v8 - (v3 + 1) >= 0:
                    v7 = (v7 - v5[v8 - (v3 + 1)]) % v1
                v6[v8] = v7 if v2[v3] == -1 or v2[v3] == v8 else 0
            v5 = v6
        return v5[-1]
