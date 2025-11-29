class C1(object):

    def minInsertions(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            if v3 == '(':
                if v2 > 0 and v2 % 2:
                    v1 += 1
                    v2 -= 1
                v2 += 2
            else:
                v2 -= 1
                if v2 < 0:
                    v1 += 1
                    v2 += 2
        return v1 + v2
