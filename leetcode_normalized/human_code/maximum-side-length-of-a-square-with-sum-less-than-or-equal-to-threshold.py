class C1(object):

    def maxSideLength(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            for v1 in range(a2, len(a1)):
                for v2 in range(a2, len(a1[0])):
                    if a1[v1][v2] - a1[v1 - a2][v2] - a1[v1][v2 - a2] + a1[v1 - a2][v2 - a2] <= a3:
                        return True
            return False
        v1 = [[0 for v2 in range(len(a1[0]) + 1)] for v2 in range(len(a1) + 1)]
        for v3 in range(1, len(a1) + 1):
            for v4 in range(1, len(a1[0]) + 1):
                v1[v3][v4] = v1[v3 - 1][v4] + v1[v3][v4 - 1] - v1[v3 - 1][v4 - 1] + a1[v3 - 1][v4 - 1]
        v5, v6 = (0, min(len(a1), len(a1[0]) + 1))
        while v5 <= v6:
            v7 = v5 + (v6 - v5) // 2
            if not check(v1, v7, a2):
                v6 = v7 - 1
            else:
                v5 = v7 + 1
        return v6
