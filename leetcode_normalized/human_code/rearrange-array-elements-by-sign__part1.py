class C1(object):

    def rearrangeArray(self, a1):
        """
        """
        v1, v2 = (0, 1)
        v3 = [0] * len(a1)
        for v4 in a1:
            if v4 > 0:
                v3[v1] = v4
                v1 += 2
            else:
                v3[v2] = v4
                v2 += 2
        return v3
