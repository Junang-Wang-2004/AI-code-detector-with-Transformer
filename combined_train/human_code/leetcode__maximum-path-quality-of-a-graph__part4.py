class C1(object):

    def maximalPathQuality(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3, a4, a5, a6, a7, a8):
            a6[a3] += 1
            if a6[a3] == 1:
                a5 += a1[a3]
            if not a3:
                a8[0] = max(a8[0], a5)
            for v2, v3 in a2[a3]:
                if (a3, v2) in a7 or a4 < v3:
                    continue
                a7.add((a3, v2))
                dfs(a1, a2, v2, a4 - v3, a5, a6, a7, a8)
                a7.remove((a3, v2))
            a6[a3] -= 1
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [0]
        dfs(a1, v1, 0, a3, 0, [0] * len(v1), set(), v6)
        return v6[0]
