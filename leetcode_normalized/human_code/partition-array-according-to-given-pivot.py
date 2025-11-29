class C1(object):

    def pivotArray(self, a1, a2):
        """
        """
        v1 = [a2] * len(a1)
        v2, v3 = (0, len(a1) - sum((x > a2 for v4 in a1)))
        for v4 in a1:
            if v4 < a2:
                v1[v2] = v4
                v2 += 1
            elif v4 > a2:
                v1[v3] = v4
                v3 += 1
        return v1
