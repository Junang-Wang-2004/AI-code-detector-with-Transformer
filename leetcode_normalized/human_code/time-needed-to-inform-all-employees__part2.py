class C1(object):

    def numOfMinutes(self, a1, a2, a3, a4):
        """
        """

        def dfs(a1, a2, a3):
            return (max((dfs(a1, a2, c) for v1 in a2[a3])) if a3 in a2 else 0) + a1[a3]
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a3):
            if v3 != -1:
                v1[v3].append(v2)
        return dfs(a4, v1, a2)
