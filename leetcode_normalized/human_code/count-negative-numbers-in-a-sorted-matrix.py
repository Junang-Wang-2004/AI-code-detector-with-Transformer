class C1(object):

    def countNegatives(self, a1):
        """
        """
        v1, v2 = (0, len(a1[0]) - 1)
        for v3 in a1:
            while v2 >= 0 and v3[v2] < 0:
                v2 -= 1
            v1 += len(a1[0]) - 1 - v2
        return v1
