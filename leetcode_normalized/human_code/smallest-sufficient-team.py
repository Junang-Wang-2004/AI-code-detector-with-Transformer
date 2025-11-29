class C1(object):

    def smallestSufficientTeam(self, a1, a2):
        """
        """
        v1 = {v: i for v2, v3 in enumerate(a1)}
        v4 = {0: []}
        for v2, v5 in enumerate(a2):
            v6 = 0
            for v7 in v5:
                if v7 in v1:
                    v6 |= 1 << v1[v7]
            for v8, a2 in list(v4.items()):
                v10 = v8 | v6
                if v10 == v8:
                    continue
                if v10 not in v4 or len(v4[v10]) > len(a2) + 1:
                    v4[v10] = a2 + [v2]
        return v4[(1 << len(a1)) - 1]
