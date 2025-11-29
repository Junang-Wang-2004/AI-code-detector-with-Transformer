class C1(object):

    def minimumArea(self, a1):
        """
        """
        v1, v2, v3, v4 = (len(a1), -1, len(a1[0]), -1)
        for v5 in range(len(a1)):
            for v6 in range(len(a1[0])):
                if a1[v5][v6] == 0:
                    continue
                v1, v2, v3, v4 = (min(v1, v5), max(v2, v5), min(v3, v6), max(v4, v6))
        return (v2 - v1 + 1) * (v4 - v3 + 1)
