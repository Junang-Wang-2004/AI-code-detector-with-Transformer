class C1(object):

    def minimumSum(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = {}
        for v3, v4 in enumerate(a1):
            if v4 in v2:
                continue
            v2[v4] = v3
        v5 = v1
        for v6, v4 in enumerate(a2):
            if v4 in v2:
                v5 = min(v5, v2[v4] + v6)
        return v5 if v5 != v1 else -1
