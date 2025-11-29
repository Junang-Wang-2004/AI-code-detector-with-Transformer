class C1(object):

    def decimalRepresentation(self, a1):
        """
        """
        v1 = []
        v2 = 1
        while a1:
            a1, v4 = divmod(a1, 10)
            if v4:
                v1.append(v4 * v2)
            v2 *= 10
        v1.reverse()
        return v1
