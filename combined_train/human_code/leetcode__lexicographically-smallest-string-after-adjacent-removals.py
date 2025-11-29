class C1(object):

    def lexicographicallySmallestString(self, a1):
        """
        """
        v1 = [[False] * len(a1) for v2 in range(len(a1))]
        for v3 in range(2, len(a1) + 1, 2):
            for v4 in range(len(a1) - (v3 - 1)):
                v5 = v4 + (v3 - 1)
                if abs(ord(a1[v4]) - ord(a1[v5])) in (1, 25) and (v5 == v4 + 1 or v1[v4 + 1][v5 - 1]):
                    v1[v4][v5] = True
                    continue
                for v6 in range(v4 + 1, v5, 2):
                    if v1[v4][v6] and v1[v6 + 1][v5]:
                        v1[v4][v5] = True
                        break
        v7 = [''] * (len(a1) + 1)
        for v4 in reversed(range(len(a1))):
            v7[v4] = a1[v4] + v7[v4 + 1]
            for v5 in range(v4 + 1, len(a1), 2):
                if v1[v4][v5]:
                    v7[v4] = min(v7[v4], v7[v5 + 1])
        return v7[0]
