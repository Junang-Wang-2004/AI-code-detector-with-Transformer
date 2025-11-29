class C1(object):

    def getLargestOutlier(self, a1):
        """
        """
        v1 = float('-inf')
        v2 = sum(a1)
        v3 = collections.defaultdict(int)
        for v4 in a1:
            v3[v4] += 1
        for v4 in a1:
            if (v2 - v4) % 2:
                continue
            v5 = (v2 - v4) // 2
            if v5 in v3 and v3[v5] - int(v5 == v4) >= 1:
                v1 = max(v1, v4)
        return v1
