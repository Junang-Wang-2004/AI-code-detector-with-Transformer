class C1(object):

    def partition(self, a1):
        """
        """
        v1 = [[False] * len(a1) for v2 in range(len(a1))]
        for v2 in reversed(range(len(a1))):
            for v3 in range(v2, len(a1)):
                v1[v2][v3] = a1[v2] == a1[v3] and (v3 - v2 < 2 or v1[v2 + 1][v3 - 1])
        v4 = [[] for v5 in range(len(a1))]
        for v2 in reversed(range(len(a1))):
            for v3 in range(v2, len(a1)):
                if v1[v2][v3]:
                    if v3 + 1 < len(a1):
                        for v6 in v4[v3 + 1]:
                            v4[v2].append([a1[v2:v3 + 1]] + v6)
                    else:
                        v4[v2].append([a1[v2:v3 + 1]])
        return v4[0]
