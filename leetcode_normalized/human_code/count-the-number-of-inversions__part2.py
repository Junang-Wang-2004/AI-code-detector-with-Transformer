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
            if v2[v3] != -1:
                v6[v2[v3]] = reduce(lambda total, i: (total + v5[v3]) % v1, range(max(v2[v3] - v3, 0), v2[v3] + 1), 0)
            else:
                for v7 in range(len(v5)):
                    v6[v7] = v5[v7]
                    if v7 - 1 >= 0:
                        v6[v7] = (v6[v7] + v6[v7 - 1]) % v1
                    if v7 - (v3 + 1) >= 0:
                        v6[v7] = (v6[v7] - v5[v7 - (v3 + 1)]) % v1
            v5 = v6
        return v5[-1]
