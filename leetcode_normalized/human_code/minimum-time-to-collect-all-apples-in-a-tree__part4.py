class C1(object):

    def minTime(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3, a4):
            v1, v2 = (0, int(a3[a3]))
            for v3 in a1[a3]:
                if v3 == a2:
                    continue
                v4 = dfs(a1, a3, v3, a3)
                v1 += v4
                v2 |= bool(v4)
            return v1 + v2
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        return 2 * max(dfs(v1, -1, 0, a3) - 1, 0)
