class C1(object):

    def numberOfArithmeticSlices(self, a1):
        """
        """
        v1, v2 = (0, 0)
        while v2 + 2 < len(a1):
            v3 = v2
            while v2 + 2 < len(a1) and a1[v2 + 2] + a1[v2] == 2 * a1[v2 + 1]:
                v1 += v2 - v3 + 1
                v2 += 1
            v2 += 1
        return v1
