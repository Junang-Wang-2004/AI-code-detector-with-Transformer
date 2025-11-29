class C1(object):

    def minSkips(self, a1, a2, a3):
        """
        """

        def ceil(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = [0] * (len(a1) - 1 + 1)
        for v2, v3 in enumerate(a1):
            for v4 in reversed(range(len(v1))):
                v1[v4] = ceil(v1[v4] + v3, a2) * a2 if v2 < len(a1) - 1 else v1[v4] + v3
                if v4 - 1 >= 0:
                    v1[v4] = min(v1[v4], v1[v4 - 1] + v3)
        v5 = a3 * a2
        for v2 in range(len(a1)):
            if v1[v2] <= v5:
                return v2
        return -1
