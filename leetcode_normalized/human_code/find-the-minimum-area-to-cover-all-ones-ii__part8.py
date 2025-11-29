class C1(object):

    def minimumSum(self, a1):
        """
        """

        def minimumArea(a1, a2, a3, a4):
            v1, v2, v3, v4 = (a2 + 1, a1 - 1, a4 + 1, a3 - 1)
            for v5 in range(a1, a2 + 1):
                for v6 in range(a3, a4 + 1):
                    if a1[v5][v6] == 0:
                        continue
                    v1, v2, v3, v4 = (min(v1, v5), max(v2, v5), min(v3, v6), max(v4, v6))
            return (v2 - v1 + 1) * (v4 - v3 + 1) if v1 <= a2 else 0
        v1 = float('inf')
        for v2 in range(len(a1) - 1):
            v3 = minimumArea(v2 + 1, len(a1) - 1, 0, len(a1[0]) - 1)
            for v4 in range(len(a1[0]) - 1):
                v5 = minimumArea(0, v2, 0, v4)
                v6 = minimumArea(0, v2, v4 + 1, len(a1[0]) - 1)
                v1 = min(v1, v3 + v5 + v6)
        for v2 in range(len(a1) - 1):
            v3 = minimumArea(0, v2, 0, len(a1[0]) - 1)
            for v4 in range(len(a1[0]) - 1):
                v5 = minimumArea(v2 + 1, len(a1) - 1, 0, v4)
                v6 = minimumArea(v2 + 1, len(a1) - 1, v4 + 1, len(a1[0]) - 1)
                v1 = min(v1, v3 + v5 + v6)
        for v4 in range(len(a1[0]) - 1):
            v3 = minimumArea(0, len(a1) - 1, v4 + 1, len(a1[0]) - 1)
            for v2 in range(len(a1) - 1):
                v5 = minimumArea(0, v2, 0, v4)
                v6 = minimumArea(v2 + 1, len(a1) - 1, 0, v4)
                v1 = min(v1, v3 + v5 + v6)
        for v4 in range(len(a1[0]) - 1):
            v3 = minimumArea(0, len(a1) - 1, 0, v4)
            for v2 in range(len(a1) - 1):
                v5 = minimumArea(0, v2, v4 + 1, len(a1[0]) - 1)
                v6 = minimumArea(v2 + 1, len(a1) - 1, v4 + 1, len(a1[0]) - 1)
                v1 = min(v1, v3 + v5 + v6)
        for v2 in range(len(a1) - 2):
            v3 = minimumArea(0, v2, 0, len(a1[0]) - 1)
            for v4 in range(v2 + 1, len(a1) - 1):
                v5 = minimumArea(v2 + 1, v4, 0, len(a1[0]) - 1)
                v6 = minimumArea(v4 + 1, len(a1) - 1, 0, len(a1[0]) - 1)
                v1 = min(v1, v3 + v5 + v6)
        for v2 in range(len(a1[0]) - 2):
            v3 = minimumArea(0, len(a1) - 1, 0, v2)
            for v4 in range(v2 + 1, len(a1[0]) - 1):
                v5 = minimumArea(0, len(a1) - 1, v2 + 1, v4)
                v6 = minimumArea(0, len(a1) - 1, v4 + 1, len(a1[0]) - 1)
                v1 = min(v1, v3 + v5 + v6)
        return v1
