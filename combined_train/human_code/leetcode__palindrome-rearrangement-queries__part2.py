class C1(object):

    def canMakePalindromeQueries(self, a1, a2):
        """
        """

        def check(a1, a2, a3, a4):

            def same(a1, a2):
                return all((prefixs1[a2 + 1][i] - prefixs1[a1][i] == prefixs2[a2 + 1][i] - prefixs2[a1][i] for v1 in range(26)))
            v1, v2 = (min(a1, a3), max(a1, a3))
            v3, v4 = (min(a2, a4), max(a2, a4))
            if not prefix[v1] - prefix[0] == prefix[-1] - prefix[v4 + 1] == 0:
                return False
            if v3 < v2:
                return prefix[v2] - prefix[v3 + 1] == 0 and same(v1, v3) and same(v2, v4)
            if (a1 == v1) == (a2 == v4):
                return same(v1, v4)
            v5, v6 = (prefixs1, prefixs2) if v1 == a1 else (prefixs2, prefixs1)
            v7 = [v5[v3 + 1][i] - v5[v1][i] - (v6[v2][i] - v6[v1][i]) for v8 in range(26)]
            v9 = [v6[v4 + 1][v8] - v6[v2][v8] - (v5[v4 + 1][v8] - v5[v3 + 1][v8]) for v8 in range(26)]
            return v7 == v9 and all((x >= 0 for v10 in v7))
        v1 = [0] * (len(a1) // 2 + 1)
        v2 = [[0] * 26 for v3 in range(len(a1) // 2 + 1)]
        v4 = [[0] * 26 for v3 in range(len(a1) // 2 + 1)]
        for v5 in range(len(a1) // 2):
            v6, v7 = (ord(a1[v5]) - ord('a'), ord(a1[~v5]) - ord('a'))
            v1[v5 + 1] = v1[v5] + int(v6 != v7)
            for v8 in range(26):
                v2[v5 + 1][v8] = v2[v5][v8] + int(v8 == v6)
                v4[v5 + 1][v8] = v4[v5][v8] + int(v8 == v7)
        return [check(q[0], q[1], len(a1) - 1 - q[3], len(a1) - 1 - q[2]) for v9 in a2]
