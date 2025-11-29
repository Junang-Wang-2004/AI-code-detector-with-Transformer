class C1(object):

    def minimumSum(self, a1):
        """
        """
        v1 = float('inf')
        v2 = [v1] * len(a1)
        v3 = v1
        for v4 in reversed(range(len(a1))):
            v2[v4] = v3
            v3 = min(v3, a1[v4])
        v5 = v3 = v1
        for v4 in range(len(a1)):
            if v3 < a1[v4] > v2[v4]:
                v5 = min(v5, v3 + a1[v4] + v2[v4])
            v3 = min(v3, a1[v4])
        return v5 if v5 != v1 else -1
