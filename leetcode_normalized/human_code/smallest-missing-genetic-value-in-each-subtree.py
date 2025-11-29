class C1(object):

    def smallestMissingValueSubtree(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2, a3, a4):
            v1 = [a3]
            while v1:
                a3 = v1.pop()
                if a2[a3] in a4:
                    continue
                a4.add(a2[a3])
                for v3 in a1[a3]:
                    v1.append(v3)
        v1 = [1] * len(a1)
        v2 = next((v2 for v2 in range(len(a2)) if a2[v2] == 1), -1)
        if v2 == -1:
            return v1
        v3 = [[] for v4 in range(len(a1))]
        for v5 in range(1, len(a1)):
            v3[a1[v5]].append(v5)
        v6 = set()
        v7 = 1
        while v2 >= 0:
            iter_dfs(v3, a2, v2, v6)
            while v7 in v6:
                v7 += 1
            v1[v2] = v7
            v2 = a1[v2]
        return v1
