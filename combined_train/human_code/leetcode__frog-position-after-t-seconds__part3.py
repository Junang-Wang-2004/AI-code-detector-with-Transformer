class C1(object):

    def frogPosition(self, a1, a2, a3, a4):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            if not a3 or not len(a1[a4]) - (a5 != 0):
                return int(a4 == a2)
            v1 = 0
            for v2 in a1[a4]:
                if v2 == a5:
                    continue
                v1 = dfs(a1, a2, a3 - 1, v2, a4)
                if v1:
                    break
            return v1 * (len(a1[a4]) - (a5 != 0))
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = dfs(v1, a4, a3, 1, 0)
        return 1.0 / v4 if v4 else 0.0
