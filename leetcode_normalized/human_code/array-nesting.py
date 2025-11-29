class C1(object):

    def arrayNesting(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if v2 is not None:
                v3, v4 = (v2, 0)
                while a1[v3] is not None:
                    v5 = v3
                    v3 = a1[v3]
                    a1[v5] = None
                    v4 += 1
                v1 = max(v1, v4)
        return v1
