class C1(object):

    def frogPosition(self, a1, a2, a3, a4):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            if not a3 or not len(a1[a4]) - (a5 != 0):
                return float(a4 == a2)
            for v1 in a1[a4]:
                if v1 == a5:
                    continue
                v2 = dfs(a1, a2, a3 - 1, v1, a4)
                if v2:
                    break
            return v2 / (len(a1[a4]) - (a5 != 0))
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        return dfs(v1, a4, a3, 1, 0)
