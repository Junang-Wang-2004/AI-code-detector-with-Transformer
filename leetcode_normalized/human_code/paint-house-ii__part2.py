from functools import reduce

class C1(object):

    def minCostII(self, a1):
        """
        """
        if not a1:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [a1[0], [0] * v2]
        for v4 in range(1, v1):
            v5, v6 = (float('inf'), float('inf'))
            for v7 in range(v2):
                if v3[(v4 - 1) % 2][v7] < v5:
                    v5, v6 = (v3[(v4 - 1) % 2][v7], v5)
                elif v3[(v4 - 1) % 2][v7] < v6:
                    v6 = v3[(v4 - 1) % 2][v7]
            for v7 in range(v2):
                v8 = v5 if v3[(v4 - 1) % 2][v7] != v5 else v6
                v3[v4 % 2][v7] = a1[v4][v7] + v8
        return min(v3[(v1 - 1) % 2])
