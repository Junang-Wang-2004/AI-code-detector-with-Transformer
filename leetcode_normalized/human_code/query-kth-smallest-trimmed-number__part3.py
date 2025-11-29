class C1(object):

    def smallestTrimmedNumbers(self, a1, a2):
        """
        """

        def compare(a1, a2):
            for v1 in range(len(a1[a1]) - t, len(a1[a1])):
                if a1[a1][v1] < a1[a2][v1]:
                    return -1
                if a1[a1][v1] > a1[a2][v1]:
                    return 1
            return cmp(a1, a2)
        v1 = max((t for v2, v3 in a2))
        v4 = [[] for v2 in range(v1 + 1)]
        for v5, (v6, v3) in enumerate(a2):
            v4[v3].append((v6, v5))
        v7 = [0] * len(a2)
        v8 = list(range(len(a1)))
        for v3 in range(1, v1 + 1):
            if not v4[v3]:
                continue
            v8.sort(cmp=compare)
            for v6, v5 in v4[v3]:
                v7[v5] = v8[v6 - 1]
        return v7
