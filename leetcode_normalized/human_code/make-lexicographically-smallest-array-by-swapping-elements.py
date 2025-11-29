class C1(object):

    def lexicographicallySmallestArray(self, a1, a2):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])
        v2 = []
        for v3 in range(len(a1)):
            if v3 - 1 < 0 or a1[v1[v3]] - a1[v1[v3 - 1]] > a2:
                v2.append([])
            v2[-1].append(v1[v3])
        v4 = [-1] * len(a1)
        for v5 in v2:
            for v3, v6 in enumerate(sorted(v5)):
                v4[v6] = a1[v5[v3]]
        return v4
