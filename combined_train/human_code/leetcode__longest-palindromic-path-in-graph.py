class C1(object):

    def maxLen(self, a1, a2, a3):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        if len(a2) == a1 * (a1 - 1) // 2:
            v1 = [0] * 26
            for v2 in a3:
                v1[ord(v2) - ord('a')] += 1
            return 2 * sum((c // 2 for v3 in v1)) + 1 * any((v3 % 2 for v3 in v1))
        v4 = [[] for v5 in range(a1)]
        for v6, v7 in a2:
            v4[v6].append(v7)
            v4[v7].append(v6)
        v8 = [[[False] * a1 for v5 in range(a1)] for v5 in range(1 << a1)]
        for v6 in range(a1):
            v8[1 << v6][v6][v6] = True
        for v6, v7 in a2:
            if a3[v6] == a3[v7]:
                v8[1 << v6 | 1 << v7][min(v6, v7)][max(v6, v7)] = True
        v9 = 0
        for v10 in range(1, 1 << a1):
            for v6 in range(a1):
                for v7 in range(v6, a1):
                    if not v8[v10][v6][v7]:
                        continue
                    v9 = max(v9, popcount(v10))
                    for v11 in v4[v6]:
                        if v10 & 1 << v11:
                            continue
                        for v12 in v4[v7]:
                            if v10 & 1 << v12:
                                continue
                            if v11 == v12:
                                continue
                            if a3[v11] == a3[v12]:
                                v8[v10 | 1 << v11 | 1 << v12][min(v11, v12)][max(v11, v12)] = True
        return v9
