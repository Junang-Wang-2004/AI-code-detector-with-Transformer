class C1(object):

    def maxValue(self, a1, a2):
        """
        """
        v1 = [[set() if j else {0} for v2 in range(a2 + 1)] for v3 in range(len(a1) + 1)]
        for v3 in range(len(a1)):
            for v2 in range(1, len(v1[v3 + 1])):
                v1[v3 + 1][v2] = set(v1[v3][v2])
                for v4 in v1[v3][v2 - 1]:
                    v1[v3 + 1][v2].add(v4 | a1[v3])
        v5 = [[set() if v2 else {0} for v2 in range(a2 + 1)] for v3 in range(len(a1) + 1)]
        for v3 in reversed(range(len(a1))):
            for v2 in range(1, len(v5[v3])):
                v5[v3][v2] = set(v5[v3 + 1][v2])
                for v4 in v5[v3 + 1][v2 - 1]:
                    v5[v3][v2].add(v4 | a1[v3])
        return max((l ^ r for v3 in range(a2, len(a1) - a2 + 1) for v6 in v1[v3][a2] for v7 in v5[v3][a2]))
