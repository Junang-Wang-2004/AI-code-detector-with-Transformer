from functools import reduce

class C1(object):

    def dieSimulator(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def sum_mod(a1):
            return reduce(lambda x, y: (x + y) % v1, a1)
        v2 = [[1] + [0] * (a2[i] - 1) for v3 in range(6)]
        for v4 in range(a1 - 1):
            v5 = [[0] * a2[v3] for v3 in range(6)]
            for v3 in range(6):
                for v6 in range(a2[v3]):
                    for v7 in range(6):
                        if v3 == v7:
                            if v6 < a2[v3] - 1:
                                v5[v7][v6 + 1] = (v5[v7][v6 + 1] + v2[v3][v6]) % v1
                        else:
                            v5[v7][0] = (v5[v7][0] + v2[v3][v6]) % v1
            v2 = v5
        return sum_mod((sum_mod(row) for v8 in v2))
