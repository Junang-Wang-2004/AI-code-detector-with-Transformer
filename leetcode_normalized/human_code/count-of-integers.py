from functools import reduce

class C1(object):

    def count(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7

        def f(a1):
            v1 = [[0] * (a4 + 1) for v2 in range(2)]
            v1[0][0] = v1[1][0] = 1
            for v3 in reversed(range(len(a1))):
                v4 = [[0] * (a4 + 1) for v2 in range(2)]
                for v5 in range(2):
                    for v6 in range(a4 + 1):
                        for v7 in range(min(int(a1[v3]) if v5 else 9, v6) + 1):
                            v4[v5][v6] = (v4[v5][v6] + v1[int(v5 and v7 == int(a1[v3]))][v6 - v7]) % v1
                v1 = v4
            return reduce(lambda x, y: (a1 + y) % v1, (v1[1][v6] for v6 in range(a3, a4 + 1)))
        return (f(a2) - f(str(int(a1) - 1))) % v1
