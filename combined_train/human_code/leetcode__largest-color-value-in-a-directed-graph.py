class C1(object):

    def largestPathValue(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(len(a1))]
        v3 = [0] * len(a1)
        for v4, v5 in a2:
            v1[v4].append(v5)
            v3[v5] += 1
        v6 = []
        for v4 in range(len(a1)):
            if not v3[v4]:
                v6.append(v4)
        v7 = [[0] * 26 for v2 in range(len(a1))]
        v8, v9 = (-1, 0)
        while v6:
            v10 = []
            for v4 in v6:
                v9 += 1
                v7[v4][ord(a1[v4]) - ord('a')] += 1
                v8 = max(v8, v7[v4][ord(a1[v4]) - ord('a')])
                for v5 in v1[v4]:
                    for v11 in range(26):
                        v7[v5][v11] = max(v7[v5][v11], v7[v4][v11])
                    v3[v5] -= 1
                    if not v3[v5]:
                        v10.append(v5)
            v6 = v10
        return v8 if v9 == len(a1) else -1
