class C1(object):

    def minZeroArray(self, a1, a2):
        """
        """
        v1 = [{0} for v2 in range(len(a1))]
        for v3, (v4, v5, v6) in enumerate(a2):
            if all((a1[v3] in v1[v3] for v3 in range(len(v1)))):
                return v3
            for v7 in range(v4, v5 + 1):
                v1[v7] |= set((x + v6 for v8 in v1[v7]))
        return len(a2) if all((a1[v3] in v1[v3] for v3 in range(len(v1)))) else -1
