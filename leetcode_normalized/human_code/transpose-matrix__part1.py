class C1(object):

    def transpose(self, a1):
        """
        """
        v1 = [[None] * len(a1) for v2 in range(len(a1[0]))]
        for v3, v4 in enumerate(a1):
            for v5, v6 in enumerate(v4):
                v1[v5][v3] = v6
        return v1
