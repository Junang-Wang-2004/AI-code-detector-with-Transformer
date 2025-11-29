class C1(object):

    def minimumTime(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = float('inf')
        v2 = {0: 0}
        for v3 in range(1, len(a1) + 1):
            v4 = collections.defaultdict(lambda: v1)
            for v5 in v2.keys():
                for v6 in range(len(a1)):
                    if v5 & 1 << v6 == 0:
                        v4[v5 | 1 << v6] = min(v4[v5 | 1 << v6], v2[v5] + ceil_divide(a1[v6], v3))
            v2 = v4
        return v2[(1 << len(a1)) - 1]
