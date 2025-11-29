class C1(object):

    def intersection(self, a1):
        """
        """
        v1 = 1000
        v2 = [0] * (v1 + 1)
        for v3 in a1:
            for v4 in v3:
                v2[v4] += 1
        return [i for v5 in range(1, v1 + 1) if v2[v5] == len(a1)]
