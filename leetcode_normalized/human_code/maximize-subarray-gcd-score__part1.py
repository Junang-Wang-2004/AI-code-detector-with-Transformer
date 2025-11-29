class C1(object):

    def maxGCDScore(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = [0] * len(a1)
        for v2 in range(len(a1)):
            while a1[v2] & 1 == 0:
                a1[v2] >>= 1
                v1[v2] += 1
        v3 = [[] for v4 in range(max(v1) + 1)]
        for v2, v5 in enumerate(v1):
            v3[v5].append(v2)
        v6 = 0
        v7 = {}
        for v2, v8 in enumerate(a1):
            v9 = {}
            v9[v8, v1[v2]] = [v2] * 2
            for (v10, v5), v11 in v7.items():
                v12 = gcd(v10, v8)
                v13 = min(v5, v1[v2])
                if (v12, v13) not in v9:
                    v9[v12, v13] = [float('inf')] * 2
                v9[v12, v13][0] = min(v9[v12, v13][0], v11[0])
                v14 = bisect_left(v3[v13], v11[0])
                v15 = bisect_right(v3[v13], v2) - 1
                v9[v12, v13][1] = min(v9[v12, v13][1], v11[0] if v15 - v14 + 1 <= a2 else v3[v13][v15 - a2] + 1)
            v7 = v9
            for (v10, v5), v11 in v7.items():
                v6 = max(v6, v10 * (v2 - v11[0] + 1) << v5, v10 * (v2 - v11[1] + 1) << v5 + 1)
        return v6
