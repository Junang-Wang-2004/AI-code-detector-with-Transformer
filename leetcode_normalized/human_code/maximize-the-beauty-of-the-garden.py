class C1(object):

    def maximumBeauty(self, a1):
        """
        """
        v1 = {}
        v2 = [0]
        v3 = float('-inf')
        for v4, v5 in enumerate(a1):
            v2.append(v2[-1] + v5 if v5 > 0 else v2[-1])
            if not v5 in v1:
                v1[v5] = v4
                continue
            v3 = max(v3, 2 * v5 + v2[v4 + 1] - v2[v1[v5]] if v5 < 0 else v2[v4 + 1] - v2[v1[v5]])
        return v3
