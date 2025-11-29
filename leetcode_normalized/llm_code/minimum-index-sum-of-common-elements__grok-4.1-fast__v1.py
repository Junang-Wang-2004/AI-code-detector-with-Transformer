class C1(object):

    def minimumSum(self, a1, a2):
        v1 = {}
        for v2, v3 in enumerate(a2):
            if v3 not in v1:
                v1[v3] = v2
        v4 = float('inf')
        v5 = len(a1)
        for v6 in range(v5):
            if a1[v6] in v1:
                v4 = min(v4, v6 + v1[a1[v6]])
        return v4 if v4 != float('inf') else -1
