class C1(object):

    def numberOfPaths(self, a1, a2):
        """
        """
        v1 = [set() for v2 in range(a1)]
        for v3, v4 in a2:
            v1[min(v3, v4) - 1].add(max(v3, v4) - 1)
        return sum((k in v1[i] for v5 in range(a1) for v6 in v1[v5] for v7 in v1[v6]))
