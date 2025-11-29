import itertools

class C1(object):

    def profitableSchemes(self, a1, a2, a3, a4):
        """
        """
        v1 = [[0 for v2 in range(a1 + 1)] for v2 in range(a2 + 1)]
        v1[0][0] = 1
        for v3, v4 in zip(a4, a3):
            for v5 in reversed(range(a2 + 1)):
                for v6 in reversed(range(a1 - v4 + 1)):
                    v1[min(v5 + v3, a2)][v6 + v4] += v1[v5][v6]
        return sum(v1[a2]) % (10 ** 9 + 7)
