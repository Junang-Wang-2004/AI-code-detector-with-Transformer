import bisect
from functools import reduce

class C1(object):

    def countRoutes(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (a1[a2], a1[a3])
        a1.sort()
        a2, a3 = (bisect.bisect_left(a1, v2), bisect.bisect_left(a1, v3))
        v6 = [[0] * (a4 + 1) for v7 in range(len(a1))]
        v8 = [[0] * (a4 + 1) for v7 in range(len(a1))]
        for v3 in range(1, a4 + 1):
            for v9 in range(len(a1) - 1):
                v10 = a1[v9 + 1] - a1[v9]
                if v3 > v10:
                    v6[v9][v3] = (v8[v9 + 1][v3 - v10] + 2 * v6[v9 + 1][v3 - v10] % v1) % v1
                elif v3 == v10:
                    v6[v9][v3] = int(v9 + 1 == a2)
            for v9 in range(1, len(a1)):
                v10 = a1[v9] - a1[v9 - 1]
                if v3 > v10:
                    v8[v9][v3] = (v6[v9 - 1][v3 - v10] + 2 * v8[v9 - 1][v3 - v10] % v1) % v1
                elif v3 == v10:
                    v8[v9][v3] = int(v9 - 1 == a2)
        v11 = int(a2 == a3)
        for v3 in range(1, a4 + 1):
            v11 = ((v11 + v6[a3][v3]) % v1 + v8[a3][v3]) % v1
        return v11
