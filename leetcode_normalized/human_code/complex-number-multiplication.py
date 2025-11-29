class C1(object):

    def complexNumberMultiply(self, a1, a2):
        """
        """
        v1, v2 = list(map(int, a1[:-1].split('+')))
        v3, v4 = list(map(int, a2[:-1].split('+')))
        return '%d+%di' % (v1 * v3 - v2 * v4, v1 * v4 + v2 * v3)
