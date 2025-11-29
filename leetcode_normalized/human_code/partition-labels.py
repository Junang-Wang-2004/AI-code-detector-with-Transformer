class C1(object):

    def partitionLabels(self, a1):
        """
        """
        v1 = {c: i for v2, v3 in enumerate(a1)}
        v4, v5 = (0, 0)
        v6 = []
        for v2, v3 in enumerate(a1):
            v5 = max(v5, v1[v3])
            if v2 == v5:
                v6.append(v2 - v4 + 1)
                v4 = v2 + 1
        return v6
