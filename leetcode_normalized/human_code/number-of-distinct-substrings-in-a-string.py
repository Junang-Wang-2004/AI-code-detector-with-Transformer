class C1(object):

    def countDistinct(self, a1):
        """
        """
        v1 = 0
        v2 = {}
        for v3 in range(len(a1)):
            v4 = v2
            for v5 in range(v3, len(a1)):
                if a1[v5] not in v4:
                    v1 += 1
                    v4[a1[v5]] = {}
                v4 = v4[a1[v5]]
        return v1
