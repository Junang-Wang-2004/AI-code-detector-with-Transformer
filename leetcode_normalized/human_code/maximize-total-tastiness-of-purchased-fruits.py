import itertools

class C1(object):

    def maxTastiness(self, a1, a2, a3, a4):
        """
        """
        v1 = [[0] * (a4 + 1) for v2 in range(a3 + 1)]
        for v3, v4 in zip(a1, a2):
            for v5 in reversed(range(v3 // 2, a3 + 1)):
                for v6 in reversed(range(a4 + 1)):
                    if v5 - v3 >= 0:
                        v1[v5][v6] = max(v1[v5][v6], v4 + v1[v5 - v3][v6])
                    if v6 - 1 >= 0:
                        v1[v5][v6] = max(v1[v5][v6], v4 + v1[v5 - v3 // 2][v6 - 1])
        return v1[a3][a4]
