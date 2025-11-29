class C1(object):

    def largestMagicSquare(self, a1):
        """
        """

        def get_sum(a1, a2, a3):
            return a1[a3 + 1] - a1[a2]

        def check(a1, a2, a3, a4, a5, a6):
            v1, v2 = (0, 0)
            for v3 in range(a4):
                v1 += a1[a5 + v3][a6 + v3]
                v2 += a1[a5 + v3][a6 + a4 - 1 - v3]
            if v1 != v2:
                return False
            for v4 in range(a5, a5 + a4):
                if v1 != get_sum(a2[v4], a6, a6 + a4 - 1):
                    return False
            for v5 in range(a6, a6 + a4):
                if v1 != get_sum(a3[v5], a5, a5 + a4 - 1):
                    return False
            return True
        v1 = [[0] * (len(a1[0]) + 1) for v2 in range(len(a1))]
        v3 = [[0] * (len(a1) + 1) for v2 in range(len(a1[0]))]
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v1[v4][v5 + 1] = v1[v4][v5] + a1[v4][v5]
                v3[v5][v4 + 1] = v3[v5][v4] + a1[v4][v5]
        for v6 in reversed(range(1, min(len(a1), len(a1[0])) + 1)):
            for v4 in range(len(a1) - (v6 - 1)):
                for v5 in range(len(a1[0]) - (v6 - 1)):
                    if check(a1, v1, v3, v6, v4, v5):
                        return v6
        return 1
