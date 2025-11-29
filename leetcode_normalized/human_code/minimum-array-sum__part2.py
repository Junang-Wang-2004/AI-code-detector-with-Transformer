class C1(object):

    def minArraySum(self, a1, a2, a3, a4):
        """
        """
        v1 = [[sum(a1)] * (a4 + 1) for v2 in range(a3 + 1)]
        for v3 in a1:
            for v4 in reversed(range(a3 + 1)):
                for v5 in reversed(range(a4 + 1)):
                    if v4 - 1 >= 0:
                        v1[v4][v5] = min(v1[v4][v5], v1[v4 - 1][v5] - v3 + (v3 + 1) // 2)
                    if v5 - 1 >= 0:
                        if v3 - a2 >= 0:
                            v1[v4][v5] = min(v1[v4][v5], v1[v4][v5 - 1] - v3 + (v3 - a2))
                    if v4 - 1 >= 0 and v5 - 1 >= 0:
                        if v3 - a2 >= 0:
                            v1[v4][v5] = min(v1[v4][v5], v1[v4 - 1][v5 - 1] - v3 + (v3 - a2 + 1) // 2)
                        if (v3 + 1) // 2 - a2 >= 0:
                            v1[v4][v5] = min(v1[v4][v5], v1[v4 - 1][v5 - 1] - v3 + ((v3 + 1) // 2 - a2))
        return v1[a3][a4]
